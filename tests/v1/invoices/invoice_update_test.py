import unittest
import json

from tests.v1.invoices.test_util import createInvoice
from paypalrestsdk.v1.invoices import InvoiceUpdateRequest
from tests.testharness import TestHarness

class InvoiceUpdateTest(TestHarness):

    def testInvoiceUpdateTest(self):
        response = createInvoice(self.client)

        request = InvoiceUpdateRequest(response.result.id)
        request.notify_merchant(True)

        request.request_body({
            "merchant_info": {
                "email": "team-dx-clients-facilitator@getbraintree.com"
            },
            "terms": "Upon receipt of this invoice, Steve owes Sasha a soda."
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
