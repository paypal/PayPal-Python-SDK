import unittest
import responses
import base64
import json

from paypalrestsdk.core import PayPalHttpClient, RefreshTokenRequest
from paypalrestsdk.core.test.paypaltestharness import PayPalTestHarness


class SimpleRequest:

    def __init__(self, path="/", verb="GET"):
        self.path = path
        self.verb = verb
        self.headers = {}


class PayPalHttpClientTest(PayPalTestHarness):

    def setUp(self):
        self.client = PayPalHttpClient(self.environment())

    @responses.activate
    def testPayPalHttpClient_execute_fetchesAccessTokenIfNone(self):
        request = SimpleRequest("/", "POST")
        self.stub_request_with_response(request)
        self.stubaccesstokenrequest()

        self.client.execute(request)

        self.assertEqual(2, len(responses.calls))

        accesstokenrequest = responses.calls[0].request
        self.assertEqual(self.environment().base_url + "/v1/oauth2/token", accesstokenrequest.url)
        self.assertEqual("application/x-www-form-urlencoded", accesstokenrequest.headers["Content-Type"])

        expectedauthheader ="Basic {0}".format(base64.b64encode(("{0}:{1}".format(self.environment().client_id, self.environment().client_secret)).encode()).decode())
        self.assertEqual(expectedauthheader, accesstokenrequest.headers["Authorization"])
        self.assertEqual("grant_type=client_credentials", accesstokenrequest.body)

    @responses.activate
    def testPayPalHttpClient_execute_fetchesAccessTokenIfExpired(self):
        request = SimpleRequest("/", "POST")
        self.stub_request_with_response(request)

        self.client._access_token = self.simpleaccesstoken()
        self.client._access_token.expires_in = 0

        self.stubaccesstokenrequest()

        self.client.execute(request)

        self.assertEqual(2, len(responses.calls))

        accesstokenrequest = responses.calls[0].request
        self.assertEqual(self.environment().base_url + "/v1/oauth2/token", accesstokenrequest.url)

    @responses.activate
    def testPayPalHttpClient_withRefreshToken_fetchesAccessTokenWithRefreshToken(self):
        request = SimpleRequest("/", "POST")
        self.stub_request_with_response(request)

        self.client = PayPalHttpClient(self.environment(), refresh_token="refresh-token")

        self.stubaccesstokenrequest(refresh_token="refresh-token")

        self.client.execute(request)

        self.assertEqual(2, len(responses.calls))

        accesstokenrequest = responses.calls[0].request
        self.assertEqual(self.environment().base_url + "/v1/oauth2/token", accesstokenrequest.url)
        self.assertEqual("application/x-www-form-urlencoded", accesstokenrequest.headers["Content-Type"])

        expectedauthheader ="Basic {0}".format(base64.b64encode(("{0}:{1}".format(self.environment().client_id, self.environment().client_secret)).encode()).decode())
        self.assertEqual(expectedauthheader, accesstokenrequest.headers["Authorization"])
        self.assertEqual("grant_type=refresh_token&refresh_token=refresh-token", accesstokenrequest.body)

    @responses.activate
    def testPayPalHttpClient_execute_setsCommonHeaders_signsRequest(self):
        self.client._access_token = self.simpleaccesstoken()

        request = SimpleRequest("/", "POST")
        self.stub_request_with_response(request)

        self.client.execute(request)

        self.assertEqual(len(responses.calls), 1)

        actualrequest = responses.calls[0].request
        self.assertEqual(actualrequest.headers["Accept-Encoding"], "gzip")
        self.assertEqual(actualrequest.headers["Authorization"], "Bearer sample-access-token")

    @responses.activate
    def testPayPalHttpClient_execute_refreshTokenRequest(self):
        refresh_token_request = RefreshTokenRequest(self.environment(), "auth-code")
        self.stub_request_with_response(refresh_token_request)

        self.client.execute(refresh_token_request)

        self.assertEqual(len(responses.calls), 1)

        actualrequest = responses.calls[0].request
        expectedauthheader ="Basic {0}".format(base64.b64encode(("{0}:{1}".format(self.environment().client_id, self.environment().client_secret)).encode()).decode())
        self.assertEqual(actualrequest.url, self.environment().base_url + "/v1/identity/openidconnect/tokenservice")
        self.assertEqual(actualrequest.headers["Authorization"], expectedauthheader)
        self.assertEqual(actualrequest.headers["Content-Type"], "application/x-www-form-urlencoded")
        self.assertEqual(actualrequest.body, "grant_type=authorization_code&code=auth-code")

if __name__ == '__main__':
    unittest.main()
