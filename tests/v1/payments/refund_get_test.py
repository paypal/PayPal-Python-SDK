import unittest
import json

from tests.v1.payments.sale_refund_test import createRefund
from paypalrestsdk.v1.payments import RefundGetRequest
from tests.testharness import TestHarness

class RefundGetTest(TestHarness):

    def testRefundGetRequestTest(self):
        refund_response = createRefund(self.client)

        request = RefundGetRequest(refund_response.result.id)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()

