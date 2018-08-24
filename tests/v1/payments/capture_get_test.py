import unittest
import json

from tests.v1.payments.authorization_capture_test import createAuthorizationCapture
from paypalrestsdk.v1.payments import CaptureGetRequest
from tests.testharness import TestHarness

class CaptureGetTest(TestHarness):

    def testCaptureGetRequestTest(self):
        response = createAuthorizationCapture(self.client)

        request = CaptureGetRequest(response.result.id)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
