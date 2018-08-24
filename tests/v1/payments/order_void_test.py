import unittest
import json

from tests.v1.payments.order_get_test import FAKE_ID
from braintreehttp.http_error import HttpError
from paypalrestsdk.v1.payments import OrderVoidRequest
from tests.testharness import TestHarness

class OrderVoidTest(TestHarness):

    def testOrderVoidRequestTest(self):
        request = OrderVoidRequest(FAKE_ID)

        try:
            self.client.execute(request)
            self.fail()
        except HttpError as he:
            self.assertTrue("debug_id" in he.message)

if __name__ == "__main__":
    unittest.main()
