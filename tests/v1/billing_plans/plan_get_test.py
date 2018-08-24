import unittest
import json

from paypalrestsdk.v1.billing_plans import PlanGetRequest
from tests.v1.billing_plans.plan_create_test import create_plan
from tests.testharness import TestHarness

class PlanGetTest(TestHarness):

    def testPlanGetTest(self):
        create_response = create_plan(self.client)

        request = PlanGetRequest(create_response.result.id)
        get_response = self.client.execute(request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)
        retrieved_plan = get_response.result

        self.assertEqual("CREATED", retrieved_plan.state)
        self.assertIsNotNone(retrieved_plan.id)
        self.assertEqual("T-Shirt of the Month Club Plan", retrieved_plan.name)

if __name__ == "__main__":
    unittest.main()
