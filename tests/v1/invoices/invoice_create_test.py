import unittest
import json

from tests.v1.invoices.test_util import createInvoice
from tests.testharness import TestHarness

class InvoiceCreateTest(TestHarness):
    def testInvoiceCreateTest(self):
        response = createInvoice(self.client)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
