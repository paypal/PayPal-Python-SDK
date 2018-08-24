import unittest
import json

from tests.v1.invoices.test_util import createInvoice, getInvoice
from tests.testharness import TestHarness

class InvoiceGetTest(TestHarness):
    def testInvoiceGetTest(self):
        invoice_response = createInvoice(self.client)

        response = getInvoice(self.client, invoice_response.result.id)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
