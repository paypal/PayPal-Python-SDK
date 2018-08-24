import unittest

from paypalrestsdk.v1.webhooks import WebhookDeleteRequest

from tests.testharness import TestHarness
from tests.v1.webhooks import create_webhook

def delete_webhook(client, webhook_id):
    request = WebhookDeleteRequest(webhook_id)

    return client.execute(request)

class WebhookDeleteTest(TestHarness):

    def testWebhookDeleteTest(self):
        created_response = create_webhook(self.client)

        delete_response = delete_webhook(self.client, created_response.result.id)
        self.assertEqual(204, delete_response.status_code)

if __name__ == "__main__":
    unittest.main()
