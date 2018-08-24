import ssl
import platform
import requests

from braintreehttp import HttpClient
from paypalrestsdk.config import __version__
from paypalrestsdk.core.util import older_than_27
from paypalrestsdk.core import AccessTokenRequest, AccessToken, RefreshTokenRequest


USER_AGENT = "PayPalSDK/PayPal-Python-SDK %s (%s)" % \
             (__version__, "requests %s; python %s; %s" %
              (requests.__version__, platform.python_version(), "" if older_than_27() else ssl.OPENSSL_VERSION))


class PayPalHttpClient(HttpClient):
    def __init__(self, environment, refresh_token=None):
        HttpClient.__init__(self, environment)
        self._refresh_token = refresh_token
        self._access_token = None
        self.environment = environment

        self.add_injector(injector=self)

    def get_user_agent(self):
        return USER_AGENT

    def __call__(self, request):
        if "Accept-Encoding" not in request.headers:
            request.headers["Accept-Encoding"] = "gzip"

        if "Authorization" not in request.headers and not isinstance(request, AccessTokenRequest) and not isinstance(request, RefreshTokenRequest):
            if not self._access_token or self._access_token.is_expired():
                accesstokenresult = self.execute(AccessTokenRequest(self.environment, self._refresh_token)).result
                self._access_token = AccessToken(access_token=accesstokenresult.access_token,
                                                 expires_in=accesstokenresult.expires_in,
                                                 token_type=accesstokenresult.token_type)

            request.headers["Authorization"] = self._access_token.authorization_string()

