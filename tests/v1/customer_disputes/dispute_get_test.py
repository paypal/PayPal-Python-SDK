import unittest
import json
from paypalrestsdk.v1.customer_disputes import DisputeGetRequest
from tests.testharness import TestHarness

class DisputeGetTest(TestHarness):

    @unittest.skip("Need a current dispute")
    def testDisputeGetTest(self):
        request = DisputeGetRequest('PP-000-042-636-306')

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertEqual("10.15", response.result.disputed_transactions[0].gross_amount.value)
        self.assertEqual("USD", response.result.disputed_transactions[0].gross_amount.currency_code)
        self.assertEqual("MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED", response.result.reason)

if __name__ == "__main__":
    unittest.main()
