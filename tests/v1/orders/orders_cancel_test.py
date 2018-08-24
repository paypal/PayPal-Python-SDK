import unittest
import json

from braintreehttp.http_error import HttpError
from tests.v1.orders.orders_create_test import create_order
from paypalrestsdk.v1.orders import OrdersCancelRequest, OrdersGetRequest
from tests.testharness import TestHarness

class OrdersCancelTest(TestHarness):

    def testOrdersCancelTest(self):
        create_response = create_order(self.client)

        get_request = OrdersGetRequest(create_response.result.id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)

        request = OrdersCancelRequest(create_response.result.id)
        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

        try:
            get_request = OrdersGetRequest(create_response.result.id)
            get_response = self.client.execute(get_request)
            self.fail()
        except HttpError as he:
            self.assertEqual(404, he.status_code)

if __name__ == "__main__":
    unittest.main()
