import unittest
import json

from tests.v1.invoices.test_util import deleteTemplate, createTemplate

from tests.testharness import TestHarness


class TemplateDeleteTest(TestHarness):

    def testTemplateDeleteTest(self):
        create_response, _ = createTemplate(self.client)

        response = deleteTemplate(self.client, create_response.result.template_id)

        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
