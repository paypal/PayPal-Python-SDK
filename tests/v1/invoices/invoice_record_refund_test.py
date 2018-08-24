import unittest
import json

from tests.v1.invoices.test_util import createInvoiceRefund
from tests.testharness import TestHarness

class InvoiceRecordRefundTest(TestHarness):

    def testInvoiceRecordRefundTest(self):
        response, _ = createInvoiceRefund(self.client)
        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
