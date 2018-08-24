import unittest
import json

from paypalrestsdk.v1.billing_agreements import AgreementCreateRequest
from paypalrestsdk.v1.billing_plans import PlanUpdateRequest, PlanGetRequest
from tests.v1.billing_plans.plan_create_test import create_plan
from tests.testharness import TestHarness
from datetime import timedelta, datetime

def create_agreement(client, plan_id):
    body = {
        "name": "Name of Agreement",
        "description": "Agreement Description",
        "start_date": start_date_for_agreement(),
        "payer": {
            "payment_method": "paypal",
            "payer_info": {
                "email": "payer@example.com"
            }
        },
        "plan": {
            "id": plan_id
        },
        "shipping_address": {
            "line1": "Hotel Staybridge",
            "line2": "Crooke Street",
            "city": "San Jose",
            "state": "CA",
            "postal_code": "95112",
            "country_code": "US"
        },
        "override_merchant_preferences": {
            "setup_fee": {
                "currency": "USD",
                "value": "3"
            },
            "return_url": "https://example.com/return",
            "cancel_url": "https://example.com/cancel",
            "auto_bill_amount": "YES",
            "initial_fail_amount_action": "CONTINUE",
            "max_fail_attempts": "11"
        }
    }
    request = AgreementCreateRequest()
    request.request_body(body)

    return client.execute(request)

def create_and_activate_plan(client):
    create_response = create_plan(client)
    created_plan = create_response.result

    update_request = PlanUpdateRequest(created_plan.id)
    update_request.request_body([{
        "op": "replace",
        "path": "/",
        "value": {
            "state": "ACTIVE"
        }
    }])
    update_response = client.execute(update_request)

    get_request = PlanGetRequest(created_plan.id)
    get_response = client.execute(get_request)
    return get_response

def start_date_for_agreement():
    days_from_now = datetime.now() + timedelta(10)
    return days_from_now.strftime("%Y-%m-%dT%H:%M:%S+00:00")

class AgreementCreateTest(TestHarness):

    def testAgreementCreateTest(self):
        created_plan_response = create_and_activate_plan(self.client)
        self.assertEqual(200, created_plan_response.status_code)
        created_plan = created_plan_response.result

        agreement_create_response = create_agreement(self.client, created_plan.id)
        self.assertEqual(201, agreement_create_response.status_code)
        self.assertIsNotNone(agreement_create_response.result)

        created_agreement = agreement_create_response.result
        self.assertEqual(created_plan.id, created_agreement.plan.id)
        self.assertEqual("Name of Agreement", created_agreement.name)
        self.assertEqual(2, len(created_agreement.links))

if __name__ == "__main__":
    unittest.main()
