import unittest
import json

from tests.v1.invoices.test_util import createInvoice

from paypalrestsdk.v1.invoices import InvoiceQrCodeRequest
from tests.testharness import TestHarness

class InvoiceQrCodeRequestTest(TestHarness):

    def testInvoiceQrCodeRequestTest(self):
        invoice_response = createInvoice(self.client)

        request = InvoiceQrCodeRequest(invoice_response.result.id) \
            .height(500) \
            .width(500)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result.image)

if __name__ == "__main__":
    unittest.main()
