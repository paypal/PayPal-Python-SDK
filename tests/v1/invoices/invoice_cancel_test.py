import unittest
import json

from tests.v1.invoices.test_util import sendInvoice
from paypalrestsdk.v1.invoices import InvoiceCancelRequest
from tests.testharness import TestHarness

class InvoiceCancelTest(TestHarness):

    def testInvoiceCancelTest(self):
        invoice_response, id = sendInvoice(self.client)
        self.assertEqual(202, invoice_response.status_code)

        request = InvoiceCancelRequest(id)
        request.request_body({
            "subject": "Past Due",
            "note": "Nevermind!",
            "send_to_merchant": True,
            "send_to_payer": True,
        })

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
