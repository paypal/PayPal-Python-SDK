import unittest
import json

from tests.v1.invoices.test_util import createTemplate, invoice_template_attributes
from paypalrestsdk.v1.invoices import TemplateUpdateRequest
from tests.testharness import TestHarness

class TemplateUpdateTest(TestHarness):

    def testTemplateUpdateTest(self):
        create_response, cleanup = createTemplate(self.client)

        request = TemplateUpdateRequest(create_response.result.template_id)
        request.request_body(invoice_template_attributes())

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        cleanup()

if __name__ == "__main__":
    unittest.main()
