import unittest
import json

from paypalrestsdk.v1.billing_plans import PlanUpdateRequest, PlanGetRequest
from tests.v1.billing_plans.plan_create_test import create_plan
from tests.testharness import TestHarness

class PlanUpdateTest(TestHarness):
    def testActivatePlan(self):
        create_response = create_plan(self.client)
        self.assertEqual(201, create_response.status_code)
        created_plan = create_response.result

        update_request = PlanUpdateRequest(created_plan.id)
        update_request.request_body([{
            "op": "replace",
            "path": "/",
            "value": {
                "state": "ACTIVE"
            }
        }])

        update_response = self.client.execute(update_request)
        self.assertEqual(200, update_response.status_code)

        get_request = PlanGetRequest(created_plan.id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertEqual("ACTIVE", get_response.result.state)

    def testPlanUpdateRequest(self):
        create_response = create_plan(self.client)
        self.assertEqual(201, create_response.status_code)
        created_plan = create_response.result

        update_request = PlanUpdateRequest(created_plan.id)
        update_request.request_body([{
            "op": "replace",
            "path": "/merchant-preferences",
            "value": {
                "cancel_url": "https://example.com/cancel/new",
                "setup_fee": {
                    "currency": "USD",
                    "value": "5"
                }
            }
        }])

        update_response = self.client.execute(update_request)
        self.assertEqual(200, update_response.status_code)

        get_request = PlanGetRequest(created_plan.id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertEqual("https://example.com/cancel/new", get_response.result.merchant_preferences.cancel_url)
        self.assertEqual("USD", get_response.result.merchant_preferences.setup_fee.currency)
        self.assertEqual("5", get_response.result.merchant_preferences.setup_fee.value)

if __name__ == "__main__":
    unittest.main()
