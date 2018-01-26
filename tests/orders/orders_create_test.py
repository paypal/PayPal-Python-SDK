import unittest
import json

from paypalrestsdk.orders import OrdersCreateRequest
from tests.testharness import TestHarness

class OrdersCreateTest(TestHarness):
    def testOrdersCreateTest(self):
        response = create_order(self.client)

        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.id)
        self.assertIsNotNone(response.result.purchase_units)
        self.assertEqual(2, len(response.result.purchase_units))

        first_purchase_unit = response.result.purchase_units[0]
        self.assertEqual("test_ref_id1", first_purchase_unit.reference_id)
        self.assertEqual("USD", first_purchase_unit.amount.currency)
        self.assertEqual("100.00", first_purchase_unit.amount.total)
        self.assertEqual("NOT_PROCESSED", first_purchase_unit.status)

        second_purchase_unit = response.result.purchase_units[1]
        self.assertEqual("test_ref_id2", second_purchase_unit.reference_id)
        self.assertEqual("USD", second_purchase_unit.amount.currency)
        self.assertEqual("50.00", second_purchase_unit.amount.total)
        self.assertEqual("NOT_PROCESSED", second_purchase_unit.status)

        self.assertEqual("https://example.com/return", response.result.redirect_urls.return_url)
        self.assertEqual("https://example.com/cancel", response.result.redirect_urls.cancel_url)

        self.assertIsNotNone(response.result.create_time)

        self.assertIsNotNone(response.result.links)

        found_approval_url = False
        for link in response.result.links:
            if "approval_url" == link.rel:
                found_approval_url = True
                self.assertIsNotNone(link.href)
                self.assertEqual("REDIRECT", link.method)
        self.assertTrue(found_approval_url)

        self.assertEqual("CREATED", response.result.status)

def create_order(client):
    request = OrdersCreateRequest()
    body = {
        "intent": "SALE",
        "purchase_units": [{
            "reference_id": "test_ref_id1",
            "amount": {
                "total": "100.00",
                "currency": "USD"
            }
        }, {
            "reference_id": "test_ref_id2",
            "amount": {
                "total": "50.00",
                "currency": "USD"
            }
        }],
        "redirect_urls": {
            "cancel_url": "https://example.com/cancel",
            "return_url": "https://example.com/return"
        }
    }
    request.request_body(body)
    return client.execute(request)

if __name__ == "__main__":
    unittest.main()
