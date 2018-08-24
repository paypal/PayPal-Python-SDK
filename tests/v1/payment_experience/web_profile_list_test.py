import unittest
import json

from paypalrestsdk.v1.payment_experience import WebProfileListRequest
from tests.v1.payment_experience.web_profile_create_test import create_web_profile
from tests.testharness import TestHarness

class WebProfileListTest(TestHarness):

    def testWebProfileListTest(self):
        create_response = create_web_profile(self.client)
        self.assertEqual(201, create_response.status_code)

        list_request = WebProfileListRequest()

        list_response = self.client.execute(list_request)
        self.assertEqual(200, list_response.status_code)
        self.assertIsNotNone(list_response.result)

        self.assertTrue(len(list_response.result) > 0)

if __name__ == "__main__":
    unittest.main()
