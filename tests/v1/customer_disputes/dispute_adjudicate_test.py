import unittest
import json

from paypalrestsdk.v1.customer_disputes import DisputeAdjudicateRequest
from tests.testharness import TestHarness

class DisputeAdjudicateTest(TestHarness):

    @unittest.skip("Need a dispute in the right state")
    def testDisputeAdjudicateTest(self):
        request = DisputeAdjudicateRequest('PP-000-042-635-209')
        request.request_body({
            "adjudication_outcome": "BUYER_FAVOR"
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
