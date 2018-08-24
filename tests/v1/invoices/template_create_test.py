import unittest
import json

from tests.v1.invoices.test_util import createTemplate
from tests.testharness import TestHarness

class TemplateCreateTest(TestHarness):

    def testTemplateCreateTest(self):
        response, cleanup = createTemplate(self.client)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

        cleanup()

if __name__ == "__main__":
    unittest.main()
