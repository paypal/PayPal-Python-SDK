import unittest
import json

from paypalrestsdk.v1.billing_plans import PlanListRequest
from tests.v1.billing_plans.plan_create_test import create_plan
from tests.testharness import TestHarness

class PlanListTest(TestHarness):

    def testPlanListTest(self):
        create_response = create_plan(self.client)

        request = PlanListRequest()
        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        plan_list = response.result
        first_plan = plan_list.plans[0]
        self.assertIsNotNone(first_plan.id)
        self.assertIsNotNone(first_plan.name)

if __name__ == "__main__":
    unittest.main()
