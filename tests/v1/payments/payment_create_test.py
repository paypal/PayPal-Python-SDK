import unittest
import json

from paypalrestsdk.v1.payments import PaymentCreateRequest
from tests.testharness import TestHarness

class PaymentCreateTest(TestHarness):
    def testPaymentCreateRequestTest(self):
        response = createPayment(self.client, "sale")
        self.assertEqual(201, response.status_code)

def createPayment(client, intent, payment_method="credit_card", invoice_number=None):
    request = PaymentCreateRequest()
    body = {
        "intent": intent,
        "transactions": [{
            "amount": {
                "total": "10",
                "currency": "USD"
            }
        }],
        "redirect_urls": {
            "cancel_url": "https://example.com/cancel",
            "return_url": "https://example.com/return"
        }
    }

    if invoice_number:
        body["transactions"][0]["invoice_number"] = invoice_number

    if payment_method is "credit_card":
        body["payer"] = {
            "payment_method": "credit_card",
            "funding_instruments": [{
                "credit_card": {
                    "billing_address": {
                        "line1": "123 Townsend st",
                        "line2": "Suite 600",
                        "city": "San Francisco",
                        "state": "CA",
                        "country_code": "US",
                        "postal_code": "94117"
                    },
                    "cvv2": "617",
                    "expire_month": 1,
                    "expire_year": 2020,
                    "first_name": "Joe",
                    "last_name": "shopper",
                    "type": "visa",
                    "number": "4422009910903049"
                }
            }]
        }
    else:
        body["payer"] = {
            "payment_method": "paypal"
        }

    request.request_body(body)
    return client.execute(request)

if __name__ == "__main__":
    unittest.main()
