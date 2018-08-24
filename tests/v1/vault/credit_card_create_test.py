import unittest
import json

from paypalrestsdk.v1.vault import CreditCardCreateRequest
from tests.testharness import TestHarness

def create_credit_card(client):
    body = {
        "number": "4417119669820331",
        "type": "visa",
        "expire_month": "11",
        "expire_year": "2055",
        "first_name": "Bobby",
        "last_name": "Smith",
        "billing_address": {
            "line1": "52 N Main St.",
            "city": "Johnstown",
            "country_code": "US",
            "postal_code": "43210",
            "state": "OH"
        }
    }

    request = CreditCardCreateRequest()
    request.request_body(body)
    return client.execute(request)

class CreditCardCreateTest(TestHarness):
    def testCreditCardCreateTest(self):
        create_response = create_credit_card(self.client)
        self.assertEqual(201, create_response.status_code)
        self.assertIsNotNone(create_response.result)

        self.assertIsNotNone(create_response.result.id)
        self.assertEqual("Bobby", create_response.result.first_name)
        self.assertEqual("Smith", create_response.result.last_name)

if __name__ == "__main__":
    unittest.main()
