import unittest
import json

from tests.v1.invoices.test_util import sendInvoice

from tests.testharness import TestHarness


class InvoiceSendTest(TestHarness):
    def testInvoiceSendTest(self):
        response, _ = sendInvoice(self.client)
        self.assertEqual(202, response.status_code)
        self.assertIsNone(response.result)


if __name__ == "__main__":
    unittest.main()
