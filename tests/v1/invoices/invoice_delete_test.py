import unittest
import json

from tests.v1.invoices.test_util import createInvoice

from paypalrestsdk.v1.invoices import InvoiceDeleteRequest
from tests.testharness import TestHarness

class InvoiceDeleteTest(TestHarness):
    def testInvoiceDeleteTest(self):
        response = createInvoice(self.client)

        request = InvoiceDeleteRequest(response.result.id)

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)


if __name__ == "__main__":
    unittest.main()
