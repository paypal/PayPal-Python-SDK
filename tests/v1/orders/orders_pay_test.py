import unittest
import json

from paypalrestsdk.v1.orders import OrdersPayRequest
from tests.testharness import TestHarness

class OrdersPayTest(TestHarness):
    def testOrdersPayTest(self):
        self.skipTest("Tests that use this class must be ignored when run in an automated environment because executing an order will require approval via the order's approval_url")

        order_id = "4KR73208J46569503"
        request = OrdersPayRequest(order_id)
        request.request_body({
            "disbursement_mode": "INSTANT"
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertEqual(order_id, response.result.order_id)
        self.assertEqual("APPROVED", response.result.status)

if __name__ == "__main__":
    unittest.main()
