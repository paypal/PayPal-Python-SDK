import unittest
import json

from paypalrestsdk.v1.payment_experience import WebProfileDeleteRequest
from tests.v1.payment_experience.web_profile_create_test import create_web_profile
from tests.testharness import TestHarness

class WebProfileDeleteTest(TestHarness):

    def testWebProfileDeleteTest(self):
        create_response = create_web_profile(self.client)
        self.assertEqual(201, create_response.status_code)

        delete_request = WebProfileDeleteRequest(create_response.result.id)
        delete_response = self.client.execute(delete_request)
        self.assertEqual(204, delete_response.status_code)

if __name__ == "__main__":
    unittest.main()
