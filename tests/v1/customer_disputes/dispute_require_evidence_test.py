import unittest
import json

from paypalrestsdk.v1.customer_disputes import DisputeRequireEvidenceRequest
from tests.testharness import TestHarness

class DisputeRequireEvidenceTest(TestHarness):

    @unittest.skip("Need a dispute in the correct state")
    def testDisputeRequireEvidenceTest(self):
        request = DisputeRequireEvidenceRequest('PP-000-042-636-306')
        request.request_body({
            "action": "SELLER_EVIDENCE"
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
