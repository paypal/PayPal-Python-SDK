import unittest
import json

from paypalrestsdk.v1.payments import AuthorizationCaptureRequest
from tests.v1.payments.payment_create_test import createPayment
from tests.testharness import TestHarness

def createAuthorizationCapture(client):
    response = createPayment(client, "authorize")
    authId = response.result.transactions[0].related_resources[0].authorization.id

    capture = {
        "amount": {
            "total": "10",
            "currency": "USD"
        },
        "is_final_capture": True
    }

    request = AuthorizationCaptureRequest(authId)
    request.request_body(capture)

    return client.execute(request)

class AuthorizationCaptureTest(TestHarness):

    def testAuthorizationCaptureRequestTest(self):
        response = createAuthorizationCapture(self.client)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
