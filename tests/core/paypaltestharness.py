from braintreehttp.testutils import TestHarness
from paypalrestsdk.core.access_token import AccessToken
from paypalrestsdk.core.environment import PayPalEnvironment
from paypalrestsdk.core.access_token_request import AccessTokenRequest

OAUTH_PATH = "/v1/oauth2/token"
OPENID_CONNECT_PATH = "/v1/identity/openidconnect/tokenservice"


class PayPalTestHarness(TestHarness):

    def environment(self):
        return PayPalEnvironment("client-id", "client-secret", "http://localhost", "http://localhost/web")

    def stubaccesstokenrequest(self, refresh_token=None, access_token_json=None):
        if not access_token_json:
            access_token_json = self.access_token_response()

        request = AccessTokenRequest(self.environment(), refresh_token)

        self.stub_request_with_response(request, access_token_json, 200)

    def simpleaccesstoken(self):
        return AccessToken("sample-access-token", 3600, "Bearer")

    def access_token_response(self, refresh_token=None):
        at = self.simpleaccesstoken()
        resp = {
            "access_token": at.access_token,
            "expires_in": at.expires_in,
            "token_type": at.token_type
        }
        if refresh_token:
            resp["refresh_token"] = refresh_token

        return resp
