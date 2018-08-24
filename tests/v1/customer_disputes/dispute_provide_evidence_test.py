import unittest
import json
import os

from braintreehttp import File
from braintreehttp import FormPart

from paypalrestsdk.v1.customer_disputes import DisputeProvideEvidenceRequest
from tests.testharness import TestHarness

class DisputeProvideEvidenceTest(TestHarness):

    @unittest.skip("Need a dispute in the correct state")
    def testDisputeProvideEvidenceTest(self):
        f = File(os.path.join(os.path.dirname(os.path.dirname(__file__)), '../resources/fileupload_test_binary.jpg'))
        request = DisputeProvideEvidenceRequest('PP-000-042-636-223')
        request.request_body({
            "input": FormPart({
                "evidence_type": 'OTHER',
                "notes": 'Notes'
            }, {
                "Content-Type": "application/json"
            }),
            "file1": f
        })
        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
