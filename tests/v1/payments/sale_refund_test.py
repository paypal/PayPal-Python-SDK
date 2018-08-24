import unittest
import json

from tests.v1.payments.payment_create_test import createPayment
from paypalrestsdk.v1.payments import SaleRefundRequest
from tests.testharness import TestHarness

def createRefund(client):
    response = createPayment(client, "sale")

    saleId = response.result.transactions[0].related_resources[0].sale.id
    request = SaleRefundRequest(saleId)
    request.request_body({})

    return client.execute(request)

class SaleRefundTest(TestHarness):

    def testSaleRefundRequestTest(self):
        response = createRefund(self.client)
        self.assertEqual(201, response.status_code)

if __name__ == "__main__":
    unittest.main()
