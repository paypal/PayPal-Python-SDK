import unittest
import json

from paypalrestsdk.v1.customer_disputes import DisputeAcceptClaimRequest
from tests.testharness import TestHarness

class DisputeAcceptClaimTest(TestHarness):

    @unittest.skip("Need a dispute in the right state")
    def testDisputeAcceptClaimTest(self):
        request = DisputeAcceptClaimRequest('PP-000-042-635-209')
        request.request_body({
            "note": "Accepting claim"
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
