import unittest

from paypalrestsdk.v1.vault import CreditCardUpdateRequest, CreditCardGetRequest

from tests.testharness import TestHarness
from tests.v1.vault import create_credit_card

class CreditCardUpdateTest(TestHarness):
    def testCreditCardUpdateTest(self):
        create_response = create_credit_card(self.client)
        self.assertEqual(201, create_response.status_code)

        update_request = CreditCardUpdateRequest(create_response.result.id)
        update_request.request_body([{
            "op": "replace",
            "path": "/billing_address/line1",
            "value": "123 East 4th St."
        }])
        update_response = self.client.execute(update_request)
        self.assertEqual(200, update_response.status_code)
        self.assertIsNotNone(update_response.result)

        get_request = CreditCardGetRequest(create_response.result.id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertEqual("123 East 4th St.", get_response.result.billing_address.line1)

if __name__ == "__main__":
    unittest.main()
