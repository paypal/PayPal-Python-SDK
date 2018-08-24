import unittest
import json

from braintreehttp.http_error import HttpError
from paypalrestsdk.v1.webhooks import WebhookCreateRequest, WebhookDeleteRequest, WebhookListRequest
from random import *
from tests.testharness import TestHarness

def create_webhook(client):
    request = WebhookCreateRequest()
    request.request_body({
        "url": 'https://example.com/webhook/python/{}'.format(randint(1, 32000)),
        "event_types": [{
            "name": "PAYMENT.AUTHORIZATION.CREATED"
        }, {
            "name": "PAYMENT.AUTHORIZATION.VOIDED"
        }]
    })

    try:
        return client.execute(request)
    except HttpError as he:
        if "NUMBER_LIMIT_EXCEEDED" in he.message:
            list_webhooks_response = client.execute(WebhookListRequest())
            for hook in list_webhooks_response.result.webhooks:
                client.execute(WebhookDeleteRequest(hook.id))
            return client.execute(request)
        else:
            raise he

class WebhookCreateTest(TestHarness):
    def testWebhookCreateTest(self):
        create_response = create_webhook(self.client)
        self.assertEqual(201, create_response.status_code)
        self.assertIsNotNone(create_response.result)
        self.assertTrue("https://example.com/webhook/python" in create_response.result.url)

if __name__ == "__main__":
    unittest.main()
