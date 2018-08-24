import unittest
import json

from paypalrestsdk.v1.webhooks import AvailableEventTypeListRequest
from tests.testharness import TestHarness

class AvailableEventTypeListTest(TestHarness):

    def testAvailableEventTypeListTest(self):
        request = AvailableEventTypeListRequest()

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)
        self.assertTrue(len(response.result.event_types) > 0)

if __name__ == "__main__":
    unittest.main()
