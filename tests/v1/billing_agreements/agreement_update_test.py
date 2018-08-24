import unittest
import json

from paypalrestsdk.v1.billing_agreements import AgreementUpdateRequest, AgreementGetRequest
from tests.testharness import TestHarness

class AgreementUpdateTest(TestHarness):
    def testAgreementUpdateTest(self):
        agreement_id = "I-4ANMVNT6VV6T"

        update_request = AgreementUpdateRequest(agreement_id)
        update_request.request_body([{
            "op": "replace",
            "path": "/",
            "value": {
                "description": "Updated description Python",
                "start_date": "2020-12-22T01:23:45Z"
            }
        }])

        update_response = self.client.execute(update_request)
        self.assertEqual(200, update_response.status_code)

        get_request = AgreementGetRequest(agreement_id)
        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertEqual("Updated description Python", get_response.result.description)

if __name__ == "__main__":
    unittest.main()
