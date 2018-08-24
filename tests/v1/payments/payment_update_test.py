import unittest
import json

from tests.v1.payments.payment_create_test import createPayment
from paypalrestsdk.v1.payments import PaymentUpdateRequest
from tests.testharness import TestHarness

class PaymentUpdateTest(TestHarness):

    def testPaymentUpdateRequestTest(self):
        payment_response = createPayment(self.client, "sale", payment_method="paypal")

        request = PaymentUpdateRequest(payment_response.result.id)
        request.request_body([{
            "path": "/transactions/0/amount",
            "op": "replace",
            "value": {
                "currency": "USD",
                "total": "11"
            }
        }])

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()

