import unittest
import json

from paypalrestsdk.v1.payment_experience import WebProfilePartialUpdateRequest, WebProfileGetRequest
from tests.v1.payment_experience.web_profile_create_test import create_web_profile
from tests.testharness import TestHarness

class WebProfilePartialUpdateTest(TestHarness):
    def testWebProfilePartialUpdateTest(self):
        create_response = create_web_profile(self.client)
        self.assertEqual(201, create_response.status_code)

        update_request = WebProfilePartialUpdateRequest(create_response.result.id)
        update_request.request_body([{
            "op": "replace",
            "path": "/presentation/brand_name",
            "value": "new_brand_name"
        }, {
            "op": "remove",
            "path": "/flow_config/landing_page_type",
        }])
        update_response = self.client.execute(update_request)
        self.assertEqual(204, update_response.status_code)

        get_request = WebProfileGetRequest(create_response.result.id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)

        self.assertEqual(create_response.result.id, get_response.result.id)
        self.assertEqual("new_brand_name", get_response.result.presentation.brand_name)
        self.assertFalse(hasattr(get_response.result.flow_config, 'landing_page_type'))

if __name__ == "__main__":
    unittest.main()
