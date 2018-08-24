import unittest
import json

from paypalrestsdk.v1.billing_plans import PlanCreateRequest
from tests.testharness import TestHarness

def create_plan(client):
    body ={
        "payment_definitions": [{
            "amount": {
                "currency": "USD",
                "value": "100"
            },
            "frequency": "MONTH",
            "cycles": "12",
            "frequency_interval": "2",
            "type": "REGULAR",
            "name": "Regular Payments",
            "charge_models": [{
                "type": "SHIPPING",
                "amount": {
                    "currency": "USD",
                    "value": "10"
                }
            }, {
                "type": "TAX",
                "amount": {
                    "currency": "USD",
                    "value": "12"
                }
            }]
        }],
        "merchant_preferences": {
            "return_url": "https://example.com/return",
            "cancel_url": "https://example.com/cancel"
        },
        "name": "T-Shirt of the Month Club Plan",
        "description": "T-Shirt Billing Plan",
        "type": "FIXED"
    }
    request = PlanCreateRequest()
    request.request_body(body)

    return client.execute(request)

class PlanCreateTest(TestHarness):
    def testPlanCreateTest(self):
        response = create_plan(self.client)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        created_plan = response.result
        self.assertEqual("CREATED", created_plan.state)
        self.assertIsNotNone(created_plan.id)
        self.assertEqual("T-Shirt of the Month Club Plan", created_plan.name)

if __name__ == "__main__":
    unittest.main()
