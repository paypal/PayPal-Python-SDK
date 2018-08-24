import unittest
import json

from paypalrestsdk.v1.payments import PaymentListRequest
from tests.testharness import TestHarness

class PaymentListTest(TestHarness):

    def testPaymentListRequestTest(self):
        request = PaymentListRequest().count(10)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.result.payments) <= 10)

if __name__ == "__main__":
    unittest.main()
