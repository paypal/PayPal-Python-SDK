import unittest
import json

from paypalrestsdk.v1.payment_experience import WebProfileUpdateRequest, WebProfileGetRequest
from random import *
from tests.v1.payment_experience.web_profile_create_test import create_web_profile
from tests.testharness import TestHarness

class WebProfileUpdateTest(TestHarness):
    def testWebProfileUpdateTest(self):
        create_response = create_web_profile(self.client)
        self.assertEqual(201, create_response.status_code)

        update_request = WebProfileUpdateRequest(create_response.result.id)
        update_request.request_body({
            "name": "Template {}".format(randint(1, 32000)),
            "flow_config": {
                "landing_page_type": "Billing",
                "bank_txn_pending_url": "http://example.com/updated",
                "user_action": "commit",
                "return_uri_http_method": "GET"
            },
            "presentation": {
                "logo_image": "http://example.com/flow_config_logo.png",
                "brand_name": "Example",
                "locale_code": "US"
            },
            "input_fields": {
                "allow_note": True,
                "no_shipping": 1,
                "address_override": 0
            },
            "temporary": False
        })

        update_response = self.client.execute(update_request)
        self.assertEqual(204, update_response.status_code)

        get_request = WebProfileGetRequest(create_response.result.id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)

        self.assertEqual(create_response.result.id, get_response.result.id)
        self.assertEqual("http://example.com/updated", get_response.result.flow_config.bank_txn_pending_url)

if __name__ == "__main__":
    unittest.main()
