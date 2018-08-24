import unittest
import json

from tests.v1.invoices.test_util import sendInvoice
from paypalrestsdk.v1.invoices import InvoiceRemindRequest
from tests.testharness import TestHarness

class InvoiceRemindTest(TestHarness):

    def testInvoiceRemindTest(self):
        invoice_response, id = sendInvoice(self.client)
        self.assertEqual(202, invoice_response.status_code)

        request = InvoiceRemindRequest(id)
        request.request_body({
            "subject": "Past due",
            "note": "Please pay soon",
            "send_to_merchant": True
        })

        response = self.client.execute(request)
        self.assertEqual(202, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
