import unittest
import json

from tests.v1.invoices.test_util import createInvoiceRefund, getInvoice
from paypalrestsdk.v1.invoices import InvoiceDeleteExternalRefundRequest
from tests.testharness import TestHarness

class InvoiceDeleteExternalRefundTest(TestHarness):

    def testInvoiceDeleteExternalRefundTest(self):
        invoice_create_response, invoice_id = createInvoiceRefund(self.client)

        invoice_get_response = getInvoice(self.client, invoice_id)

        request = InvoiceDeleteExternalRefundRequest(invoice_id, invoice_get_response.result.refunds[0].transaction_id)

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

if __name__ == "__main__":
    unittest.main()
