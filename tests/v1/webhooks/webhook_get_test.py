import unittest

from paypalrestsdk.v1.webhooks import WebhookGetRequest

from tests.testharness import TestHarness
from tests.v1.webhooks import create_webhook

class WebhookGetTest(TestHarness):

    def testWebhookGetTest(self):
        created_response = create_webhook(self.client)

        request = WebhookGetRequest(created_response.result.id)
        get_response = self.client.execute(request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)
        self.assertEqual(created_response.result.id, get_response.result.id)

if __name__ == "__main__":
    unittest.main()
