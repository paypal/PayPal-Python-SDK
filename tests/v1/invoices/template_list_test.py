import unittest
import json

from tests.v1.invoices.test_util import createTemplate

from paypalrestsdk.v1.invoices import TemplateListRequest
from tests.testharness import TestHarness


class TemplateListTest(TestHarness):

    def testTemplateGetTemplatesTest(self):
        _, cleanup = createTemplate(self.client)

        request = TemplateListRequest()
        request.fields("none")

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertTrue(len(response.result.templates) >= 1)

        cleanup()

if __name__ == "__main__":
    unittest.main()
