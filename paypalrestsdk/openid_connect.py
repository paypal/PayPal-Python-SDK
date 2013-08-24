from paypalrestsdk.resource import Resource
import paypalrestsdk.util as util
import paypalrestsdk.api as api
from paypalrestsdk.version import __version__


class Base(Resource):

    user_agent = "PayPalSDK/openid-connect-python %s (%s)" % (__version__, api.Api.library_details)

    @classmethod
    def post(cls, action, options={}, headers={}):
        url = util.join_url(endpoint(), action)
        body = util.urlencode(options)
        headers = util.merge_dict({
            'User-Agent': cls.user_agent,
            'Content-Type': 'application/x-www-form-urlencoded'}, headers)
        data = api.default().http_call(url, 'POST', body=body, headers=headers)
        return cls(data)


class Tokeninfo(Base):

    path = "v1/identity/openidconnect/tokenservice"

    @classmethod
    def create(cls, options={}):
        if isinstance(options, str):
            options = {'code': options}

        options = util.merge_dict({
            'grant_type': 'authorization_code',
            'client_id': client_id(),
            'client_secret': client_secret()
        }, options)

        return cls.post(cls.path, options)

    @classmethod
    def create_with_refresh_token(cls, options={}):
        if isinstance(options, str):
            options = {'refresh_token': options}

        options = util.merge_dict({
            'grant_type': 'refresh_token',
            'client_id': client_id(),
            'client_secret': client_secret()
        }, options)

        return cls.post(cls.path, options)

    @classmethod
    def authorize_url(cls, options={}):
        return authorize_url(options)

    def logout_url(self, options={}):
        options = util.merge_dict({'id_token': self.id_token}, options)
        return logout_url(options)

    def refresh(self, options={}):
        options = util.merge_dict({'refresh_token': self.refresh_token}, options)
        tokeninfo = self.__class__.create_with_refresh_token(options)
        self.merge(tokeninfo.to_dict())
        return self

    def userinfo(self, options={}):
        options = util.merge_dict({'access_token': self.access_token}, options)
        return Userinfo.get(options)


class Userinfo(Base):

    path = "v1/identity/openidconnect/userinfo"

    @classmethod
    def get(cls, options={}):
        if isinstance(options, str):
            options = {'access_token': options}
        options = util.merge_dict({'schema': 'openid'}, options)

        return cls.post(cls.path, options)


def endpoint():
    return api.default().options.get("openid_endpoint", "https://api.paypal.com/")


def client_id():
    return api.default().options.get("openid_client_id", api.default().client_id)


def client_secret():
    return api.default().options.get("openid_client_secret", api.default().client_secret)


def redirect_uri():
    return api.default().options.get("openid_redirect_uri")


start_session_path = "https://www.paypal.com/webapps/auth/protocol/openidconnect/v1/authorize"
end_session_path = "https://www.paypal.com/webapps/auth/protocol/openidconnect/v1/endsession"


def authorize_url(options={}):
    options = util.merge_dict({
        'response_type': 'code',
        'scope': 'openid',
        'client_id': client_id(),
        'redirect_uri': redirect_uri()
    }, options)
    return util.join_url_params(start_session_path, options)


def logout_url(options={}):
    options = util.merge_dict({
        'logout': 'true',
        'redirect_uri': redirect_uri()
    }, options)
    return util.join_url_params(end_session_path, options)
