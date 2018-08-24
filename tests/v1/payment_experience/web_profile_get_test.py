import unittest
import json

from paypalrestsdk.v1.payment_experience import WebProfileGetRequest
from tests.v1.payment_experience.web_profile_create_test import create_web_profile
from tests.testharness import TestHarness

class WebProfileGetTest(TestHarness):

    def testWebProfileGetTest(self):
        create_response = create_web_profile(self.client)
        self.assertEqual(201, create_response.status_code)

        get_request = WebProfileGetRequest(create_response.result.id)

        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)

        self.assertEqual(create_response.result.id, get_response.result.id)

if __name__ == "__main__":
    unittest.main()
