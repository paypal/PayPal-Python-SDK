import unittest
import json

from tests.v1.invoices.test_util import createInvoice
from paypalrestsdk.v1.invoices import InvoiceSearchRequest
from tests.testharness import TestHarness

class InvoiceSearchTest(TestHarness):

    def testInvoiceSearchTest(self):
        invoice_send_response = createInvoice(self.client)

        request = InvoiceSearchRequest()
        request.request_body({
            "number": invoice_send_response.result.number
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.result.invoices))
        self.assertEqual(invoice_send_response.result.id, response.result.invoices[0].id)

if __name__ == "__main__":
    unittest.main()
