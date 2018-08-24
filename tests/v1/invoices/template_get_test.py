import unittest
import json

from tests.v1.invoices.test_util import createTemplate

from paypalrestsdk.v1.invoices import TemplateGetRequest
from tests.testharness import TestHarness


class TemplateGetTest(TestHarness):

    def testTemplateGetTest(self):
        create_response, cleanup = createTemplate(self.client)

        response = self.client.execute(TemplateGetRequest(create_response.result.template_id))
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        cleanup()

if __name__ == "__main__":
    unittest.main()
