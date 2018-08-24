import unittest
import json

from paypalrestsdk.v1.payments import AuthorizationGetRequest
from tests.v1.payments.payment_create_test import createPayment
from tests.testharness import TestHarness

class AuthorizationGetTest(TestHarness):

    def testAuthorizationGetRequestTest(self):
        payment_response = createPayment(self.client, "authorize")
        authId = payment_response.result.transactions[0].related_resources[0].authorization.id

        request = AuthorizationGetRequest(authId)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
