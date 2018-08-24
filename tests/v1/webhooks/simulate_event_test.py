import unittest
import json

from paypalrestsdk.v1.webhooks import SimulateEventRequest
from tests.testharness import TestHarness

class SimulateEventTest(TestHarness):
    def testSimulateEventTest(self):
        request = SimulateEventRequest()
        request.request_body({
            "url": "https://www.example.com/paypal_webhook",
            "event_type": "PAYMENT.AUTHORIZATION.CREATED"
        })

        response = self.client.execute(request)
        self.assertEqual(202, response.status_code)
        self.assertIsNotNone(response.result)
        self.assertEqual("PAYMENT.AUTHORIZATION.CREATED", response.result.event_type)

if __name__ == "__main__":
    unittest.main()
