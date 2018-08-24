import unittest
import json

from paypalrestsdk.v1.invoices import InvoiceNextInvoiceNumberRequest
from tests.testharness import TestHarness

class InvoiceNextInvoiceNumberRequestTest(TestHarness):

    def testInvoiceNextInvoiceNumberRequestTest(self):
        request = InvoiceNextInvoiceNumberRequest()

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result.number)

if __name__ == "__main__":
    unittest.main()
