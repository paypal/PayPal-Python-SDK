import unittest
import json

from paypalrestsdk.v1.payment_experience import WebProfileCreateRequest
from random import *
from tests.testharness import TestHarness

def create_web_profile(client):
    request = WebProfileCreateRequest()

    request.request_body({
        "name": "Template {}".format(randint(1, 32000)),
        "flow_config": {
            "landing_page_type": "Billing",
            "bank_txn_pending_url": "http://example.com/flow_config_pending",
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

    return client.execute(request)


class WebProfileCreateTest(TestHarness):
    def testWebProfileCreateTest(self):
        create_response = create_web_profile(self.client)
        self.assertEqual(201, create_response.status_code)
        self.assertIsNotNone(create_response.result)

        self.assertIsNotNone(create_response.result.id)
        self.assertEqual("Billing", create_response.result.flow_config.landing_page_type)

if __name__ == "__main__":
    unittest.main()
