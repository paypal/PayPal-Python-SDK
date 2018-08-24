import unittest
import json

from paypalrestsdk.v1.webhooks import WebhookListRequest
from tests.testharness import TestHarness

def list_webhooks(client):
    request = WebhookListRequest()
    return client.execute(request)

class WebhookListTest(TestHarness):

    def testWebhookListTest(self):
        response = list_webhooks(self.client)

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
