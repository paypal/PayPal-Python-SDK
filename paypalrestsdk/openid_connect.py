import paypalrestsdk.util as util
from paypalrestsdk.resource import Resource
from paypalrestsdk.api import default as default_api
from paypalrestsdk.api import Api
from paypalrestsdk.config import __version__
from six import string_types

class Base(Resource):

    user_agent = "PayPalSDK/openid-connect-python %s (%s)" % (__version__, Api.library_details)

    @classmethod
    def post(cls, action, options=None, headers=None, api=None):
        api = api or default_api()
        url = util.join_url(endpoint(api), action)
        body = util.urlencode(options or {})
        headers = util.merge_dict({
            'User-Agent': cls.user_agent,
            'Content-Type': 'application/x-www-form-urlencoded'}, headers or {})
        data = api.http_call(url, 'POST', data=body, headers=headers)
        return cls(data)


class Tokeninfo(Base):
    """Token service for Log In with PayPal, API docs at
    https://developer.paypal.com/docs/api/#identity
    """

    path = "v1/identity/openidconnect/tokenservice"

    @classmethod
    def create(cls, options=None, api=None):
        options = options or {}
        api = api or default_api()
        if isinstance(options, string_types):
            options = {'code': options}

        options = util.merge_dict({
            'grant_type': 'authorization_code',
            'client_id': client_id(api),
            'client_secret': client_secret(api)
        }, options)
        return cls.post(cls.path, options, api=api)

    @classmethod
    def create_with_refresh_token(cls, options=None, api=None):
        options = options or {}
        api = api or default_api()
        if isinstance(options, string_types):
            options = {'refresh_token': options}
        options = util.merge_dict({
            'grant_type': 'refresh_token',
            'client_id': client_id(api),
            'client_secret': client_secret(api)
        }, options)

        return cls.post(cls.path, options, api=api)

    @classmethod
    def authorize_url(cls, options=None, api=None):
        return authorize_url(options or {}, api=api)

    def logout_url(self, options=None, api=None):
        return logout_url(util.merge_dict({'id_token': self.id_token}, options or {}), api=api)

    def refresh(self, options=None, api=None):
        options = util.merge_dict({'refresh_token': self.refresh_token}, options or {})
        tokeninfo = self.__class__.create_with_refresh_token(options, api=api)
        self.merge(tokeninfo.to_dict())
        return self

    def userinfo(self, options=None, api=None):
        return Userinfo.get(util.merge_dict({'access_token': self.access_token}, options or {}), api=api)


class Userinfo(Base):
    """Retrive user profile attributes for Log In with PayPal
    """

    path = "v1/identity/openidconnect/userinfo"

    @classmethod
    def get(cls, options=None, api=None):
        options = options or {}
        if isinstance(options, string_types):
            options = {'access_token': options}
        options = util.merge_dict({'schema': 'openid'}, options)
        api = api or default_api()
        return cls.post(cls.path, options, api=api)


def endpoint(api=None):
    api = api or default_api()
    return api.options.get("openid_endpoint", api.endpoint)


def client_id(api=None):
    api = api or default_api()
    return api.options.get("openid_client_id", api.client_id)


def client_secret(api=None):
    api = api or default_api()
    return api.options.get("openid_client_secret", api.client_secret)


def redirect_uri(api=None):
    api = api or default_api()
    return api.options.get("openid_redirect_uri")


start_session_path = "/signin/authorize"
end_session_path = "/webapps/auth/protocol/openidconnect/v1/endsession"


def session_url(path, options=None, api=None):
    api = api or default_api()
    if api.mode == "live":
        path = util.join_url("https://www.paypal.com", path)
    else:
        path = util.join_url("https://www.sandbox.paypal.com", path)
    return util.join_url_params(path, options or {})


def authorize_url(options=None, api=None):
    api = api or default_api()
    options = util.merge_dict({
        'response_type': 'code',
        'scope': 'openid',
        'client_id': client_id(api),
        'redirect_uri': redirect_uri(api)
    }, options or {})
    return session_url(start_session_path, options, api=api)


def logout_url(options=None, api=None):
    api = api or default_api()
    options = util.merge_dict({
        'logout': 'true',
        'redirect_uri': redirect_uri(api)
    }, options or {})
    return session_url(end_session_path, options, api=api)
