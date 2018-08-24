import unittest
import json

from paypalrestsdk.v1.billing_agreements import AgreementExecuteRequest
from tests.testharness import TestHarness

class AgreementExecuteTest(TestHarness):

    @unittest.skip("need a token to execute")
    def testAgreementExecuteTest(self):
        token = ""
        request = AgreementExecuteRequest(token)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        activated_agreement = response.result
        self.assertIsNotNone(activated_agreement.id)
        self.assertEqual("Active", activated_agreement.state)

if __name__ == "__main__":
    unittest.main()
