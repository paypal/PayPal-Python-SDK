import unittest
import json

from tests.orders.orders_create_test import create_order

from paypalrestsdk.orders import OrdersGetRequest
from tests.testharness import TestHarness

class OrdersGetTest(TestHarness):

    def testOrdersGetTest(self):
        create_response = create_order(self.client)

        get_request = OrdersGetRequest(create_response.result.id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)

        created_order = create_response.result
        retrieved_order = get_response.result

        self.assertEqual(created_order.id, retrieved_order.id)
        self.assertEqual(len(created_order.purchase_units), len(retrieved_order.purchase_units))

        self.assertEqual(created_order.redirect_urls.return_url, retrieved_order.redirect_urls.return_url)
        self.assertEqual(created_order.redirect_urls.cancel_url, retrieved_order.redirect_urls.cancel_url)

        self.assertEqual(created_order.create_time, retrieved_order.create_time)

        self.assertIsNotNone(retrieved_order.links)

        found_approval_url = False
        for link in retrieved_order.links:
            if "approval_url" == link.rel:
                found_approval_url = True
                self.assertIsNotNone(link.href)
                self.assertEqual("REDIRECT", link.method)
        self.assertTrue(found_approval_url)

        self.assertEqual("CREATED", retrieved_order.status)

if __name__ == "__main__":
    unittest.main()
