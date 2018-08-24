import unittest

from paypalrestsdk.core import RefreshTokenRequest, PayPalHttpClient
from paypalrestsdk.v1.identity import UserConsent, UserinfoGetRequest
from tests.testharness import TestHarness

try:
    from urlparse import urlparse, parse_qs
    from urllib import quote
except ImportError:
    from urllib.parse import quote
    from urllib.parse import urlparse, parse_qs

class UserConsentTest(TestHarness):

    def testUserConsent(self):
        consenturl = UserConsent(self.environment) \
                .response_type('code') \
                .scope('profile+email+openid+address') \
                .redirect_uri('http://example.com') \
                .nonce('some-nonce') \
                .state('some-state') \
                .build()

        url = urlparse(consenturl)

        self.assertEqual('https', url.scheme)
        self.assertEqual('www.sandbox.paypal.com', url.netloc)
        self.assertEqual('/signin/authorize', url.path)

        query_params = parse_qs(url.query)
        
        self.assertEqual(self.environment.client_id, query_params['client_id'][0])
        self.assertEqual('code', query_params['response_type'][0])
        self.assertEqual('profile email openid address', query_params['scope'][0])
        self.assertEqual('http://example.com', query_params['redirect_uri'][0])
        self.assertEqual('some-nonce', query_params['nonce'][0])
        self.assertEqual('some-state', query_params['state'][0])

    @unittest.skip('This test is an example of how to fetch a refresh token based on a code')
    def testGetRefreshTokenFromCode(self):
        redirect_uri = quote('http://requestbin.fullcontact.com/15a7bhu1')
        consenturl = UserConsent(self.environment) \
                .response_type('code') \
                .scope(quote('profile email address openid')) \
                .redirect_uri(redirect_uri) \
                .build()

        # Retreived after logging in as a customer at `consenturl`
        code = 'C21AAH5vyDshcUszNumTtlxwQCbB_pzAbSAFOZA-3CaW5I8cw8xrzZlhlykUG0XIE97irRn6hz_uJrvNe_czJc2NNW1sPvqdw'
        
        refresh_token_request = RefreshTokenRequest(self.environment, code)

        response = self.client.execute(refresh_token_request)
        self.assertEquals(200, response.status_code)
        self.assertIsNotNone(response.result.refresh_token)

    @unittest.skip('This is an example of how to fetch user info')
    def testUserInfoGetRequest(self):
        refresh_token = 'R23AAHZ-1H7nubdmwjb7hUJketmqT3gwYdITS4NKVpNW5DPGHz2TO4eqiRTwW9gIaohHEsu22wGENpsq4a7xsPkR3Zqpmq50-hgLVjs_EgwUm2rKyWkf3_FMI39Fgo_cweVp-b915SsKWIoNuxDjg'
        scoped_http_client = PayPalHttpClient(self.environment, refresh_token)

        get_info_request = UserinfoGetRequest() \
                .schema('openid')

        user_info_response = scoped_http_client.execute(get_info_request)
        
        self.assertEqual(200, user_info_response.status_code)
        self.assertIsNotNone(200, user_info_response.result)


if __name__ == "__main__":
    unittest.main()
