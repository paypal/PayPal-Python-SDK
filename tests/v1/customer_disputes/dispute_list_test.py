import unittest
import json
from paypalrestsdk.v1.customer_disputes import DisputeListRequest
from tests.testharness import TestHarness

class DisputeListTest(TestHarness):

    @unittest.skip("Need a sandbox credential with dispute access")
    def testDisputeListTest(self):
        request = DisputeListRequest()

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)
        self.assertEqual(10, len(response.result.items))

if __name__ == "__main__":
    unittest.main()
