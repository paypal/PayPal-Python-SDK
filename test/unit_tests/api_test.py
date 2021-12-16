from test_helper import unittest, client_id, client_secret, paypal
from mock import Mock, patch, ANY
from paypalrestsdk.config import __default_timeout__


class Api(unittest.TestCase):

    def setUp(self):
        self.api = paypal.Api(
            client_id=client_id,
            client_secret=client_secret
        )
        self.api.request = Mock()
        self.card_attributes = {
            "type": "visa",
            "number": "4417119669820331",
            "expire_month": "11",
            "expire_year": "2018",
            "cvv2": "874",
            "first_name": "Joe",
            "last_name": "Shopper"}
        self.authorization_code = 'auth_code_from_device'
        self.refresh_token = 'long_living_token'
        self.access_token = 'use_once_token'
        self.future_payments_scope = 'https://api.paypal.com/v1/payments/.* https://uri.paypal.com/services/payments/futurepayments'

    def test_endpoint(self):
        new_api = paypal.Api(
            mode="live", client_id="dummy", client_secret="dummy")
        self.assertEqual(new_api.endpoint, "https://api.paypal.com")
        self.assertEqual(new_api.token_endpoint, "https://api.paypal.com")

        new_api = paypal.Api(
            mode="sandbox", client_id="dummy", client_secret="dummy")
        self.assertEqual(new_api.endpoint, "https://api.sandbox.paypal.com")
        self.assertEqual(
            new_api.token_endpoint, "https://api.sandbox.paypal.com")

        new_api = paypal.Api(
            endpoint="https://custom-endpoint.paypal.com", client_id="dummy", client_secret="dummy")
        self.assertEqual(
            new_api.endpoint, "https://custom-endpoint.paypal.com")
        self.assertEqual(
            new_api.token_endpoint, "https://custom-endpoint.paypal.com")

    def test_get(self):
        payment_history = self.api.get("/v1/payments/payment?count=1")
        self.api.request.assert_called_once_with(
            'https://api.sandbox.paypal.com/v1/payments/payment?count=1', 'GET', headers={}, refresh_token=None)

    def test_post(self):
        self.api.request.return_value = {'id': 'test'}
        credit_card = self.api.post(
            "v1/vault/credit-cards", self.card_attributes)

        self.assertEqual(credit_card.get('error'), None)
        self.assertNotEqual(credit_card.get('id'), None)

    def test_bad_request(self):
        self.api.request.return_value = {'error': 'test'}
        credit_card = self.api.post("v1/vault/credit-cards", {})

        self.api.request.assert_called_once_with('https://api.sandbox.paypal.com/v1/vault/credit-cards',
                                                 'POST',
                                                 body={},
                                                 headers={},
                                                 refresh_token=None)
        self.assertNotEqual(credit_card.get('error'), None)

    @patch('test_helper.paypal.Api.http_call', autospec=True)
    def test_expired_time(self, mock):
        mock.return_value = {
            'access_token': self.access_token,
            'expires_in': 900,
            'refresh_token': self.refresh_token,
            'scope': self.future_payments_scope,
            'token_type': 'Bearer'
        }
        old_token = self.api.get_access_token()
        mock.assert_called_once_with(self.api,
                                     'https://api.sandbox.paypal.com/v1/oauth2/token',
                                     'POST',
                                     headers=ANY,
                                     data='grant_type=client_credentials',
                                     timeout=__default_timeout__
                                     )
        old_token = self.api.get_access_token()
        mock.assert_called_once_with(self.api,
                                     'https://api.sandbox.paypal.com/v1/oauth2/token',
                                     'POST',
                                     headers=ANY,
                                     data='grant_type=client_credentials',
                                     timeout=__default_timeout__,
                                     )

        self.api.token_hash["expires_in"] = 0
        new_token = self.api.get_access_token()
        self.assertEqual(len(mock.call_args_list), 2)

    def test_not_found(self):
        self.api.request.side_effect = paypal.ResourceNotFound("error")
        self.assertRaises(
            paypal.ResourceNotFound, self.api.get, ("/v1/payments/payment/PAY-1234"))

    @patch('test_helper.paypal.Api.http_call', autospec=True)
    def test_get_refresh_token(self, mock_http):
        mock_http.return_value = {
            'access_token': self.access_token,
            'expires_in': 900,
            'refresh_token': self.refresh_token,
            'scope': self.future_payments_scope,
            'token_type': 'Bearer'
        }
        refresh_token = self.api.get_refresh_token(self.authorization_code)
        mock_http.assert_called_once_with(self.api,
                                          'https://api.sandbox.paypal.com/v1/oauth2/token', 'POST',
                                          data='grant_type=authorization_code&response_type=token&redirect_uri=urn:ietf:wg:oauth:2.0:oob&code=' +
                                          self.authorization_code,
                                          headers={
                                              'Content-Type': 'application/x-www-form-urlencoded',
                                              'Accept': 'application/json',
                                              'Authorization': 'Basic ' + self.api.basic_auth(),
                                              'User-Agent': ANY
                                          },
                                          timeout=__default_timeout__
                                          )
        self.assertEqual(refresh_token, self.refresh_token)

    def test_fail_get_refresh_token(self):
        self.assertRaises(
            paypal.MissingConfig, self.api.get_refresh_token, None)

    @patch('test_helper.paypal.Api.http_call', autospec=True)
    def test_refresh_access_token(self, mock_http):
        mock_http.return_value = {
            'access_token': self.access_token,
            'app_id': 'APP-6XR95014BA15863X',
            'expires_in': 900,
            'scope': self.future_payments_scope,
            'token_type': 'Bearer'
        }
        access_token = self.api.get_token_hash(
            refresh_token=self.refresh_token, 
            headers={"test-header" : "test-value"})['access_token']

        mock_http.assert_called_once_with(self.api,
                                          'https://api.sandbox.paypal.com/v1/oauth2/token', 'POST',
                                          data='grant_type=refresh_token&refresh_token=' +
                                          self.refresh_token,
                                          headers={
                                              'Content-Type': 'application/x-www-form-urlencoded',
                                              'Accept': 'application/json',
                                              'Authorization': 'Basic ' + self.api.basic_auth(),
                                              'User-Agent': ANY,
                                              'test-header': 'test-value'
                                          },
                                          timeout=__default_timeout__
                                          )
        self.assertEqual(access_token, self.access_token)
