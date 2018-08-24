import unittest
import json

from tests.v1.invoices.test_util import createInvoicePayment, getInvoice
from paypalrestsdk.v1.invoices import InvoiceDeleteExternalPaymentRequest
from tests.testharness import TestHarness

class InvoiceDeleteExternalPaymentTest(TestHarness):

    def testInvoiceDeleteExternalPaymentTest(self):
        invoice_payment_response, invoice_id = createInvoicePayment(self.client)

        invoice_get_response = getInvoice(self.client, invoice_id)
        request = InvoiceDeleteExternalPaymentRequest(invoice_id, invoice_get_response.result.payments[0].transaction_id)

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

if __name__ == "__main__":
    unittest.main()
