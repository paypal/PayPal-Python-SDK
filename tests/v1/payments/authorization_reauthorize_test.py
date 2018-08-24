import unittest
import json

from paypalrestsdk.v1.payments import AuthorizationReauthorizeRequest
from tests.v1.payments.payment_create_test import createPayment
from tests.testharness import TestHarness

class AuthorizationReauthorizeTest(TestHarness):

    def testAuthorizationReauthorizeRequestTest(self):
        payment_response = createPayment(self.client, "authorize")
        authId = payment_response.result.transactions[0].related_resources[0].authorization.id

        request = AuthorizationReauthorizeRequest(authId)

        body = {
            "amount": {
                "total": "10",
                "currency": "USD"
            }
        }
        request.request_body(body)

        try:
            response = self.client.execute(request)
        except IOError as ioe:
            self.assertTrue("DCC_REAUTHORIZATION_NOT_ALLOWED" in ioe.message)

if __name__ == "__main__":
    unittest.main()
