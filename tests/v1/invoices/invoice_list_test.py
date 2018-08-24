import unittest
import json

from tests.v1.invoices.test_util import createInvoice
from paypalrestsdk.v1.invoices import InvoiceListRequest
from tests.testharness import TestHarness

class InvoiceListTest(TestHarness):

    def testInvoiceListTest(self):
        createInvoice(self.client)

        request = InvoiceListRequest()
        request.page(0)
        request.page_size(1)
        request.total_count_required(True)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertTrue(response.result.total_count > 0)
        self.assertTrue(len(response.result.invoices) == 1)

if __name__ == "__main__":
    unittest.main()
