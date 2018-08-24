import unittest
import json

from tests.v1.invoices.test_util import createInvoicePayment

from tests.testharness import TestHarness


class InvoiceRecordPaymentTest(TestHarness):

    def testInvoiceRecordPaymentTest(self):
        response, invoice_id = createInvoicePayment(self.client)
        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
