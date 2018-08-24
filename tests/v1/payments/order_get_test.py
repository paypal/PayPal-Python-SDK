import unittest
import json

from paypalrestsdk.v1.payments.order_get_request import OrderGetRequest
from tests.testharness import TestHarness

FAKE_ID = "O-2FK09787H36911800"

class OrderGetTest(TestHarness):

    def testOrderGetRequestTest(self):
        self.skipTest("Tests that use this class must be ignored when run in an automated environment because executing an order will require approval via the executed payment's approval_url")

        orderGetResponse = self.client.execute(OrderGetRequest(FAKE_ID))
        self.assertEqual(200, orderGetResponse.status_code)

if __name__ == "__main__":
    unittest.main()
