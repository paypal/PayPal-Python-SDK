import unittest
import json

from tests.v1.payments.order_get_test import FAKE_ID
from braintreehttp.http_error import HttpError
from paypalrestsdk.v1.payments import OrderCaptureRequest
from tests.testharness import TestHarness

class OrderCaptureTest(TestHarness):

    def testOrderCaptureRequestTest(self):

        request = OrderCaptureRequest(FAKE_ID)
        request.request_body({
            "amount": {
                "total":"10",
                "currency": "USD"
            },
            "is_final_capture": True,
        })

        try:
            self.client.execute(request)
            self.fail()
        except HttpError as he:
            # Fails with an internal service error, order does not exist
            self.assertTrue("debug_id" in he.message)

if __name__ == "__main__":
    unittest.main()
