import unittest
import json

from paypalrestsdk.v1.sync import SearchGetRequest
from tests.testharness import TestHarness

class SearchGetTest(TestHarness):

    def testSearchMultipleTransactionsBetweenDates(self):
        request = SearchGetRequest()
        request.start_date("2018-01-22T00:00:00+00:00")
        request.end_date("2018-01-23T00:00:00+00:00")

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertEqual(77, response.result.total_items)
        self.assertIsNotNone(response.result.transaction_details)
        self.assertEqual(77, len(response.result.transaction_details))

    def testSearchGetSpecifictransactionId(self):
        request = SearchGetRequest()
        transaction_id = "4LJ583775B2362642"
        request.transaction_id(transaction_id)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertIsNotNone(response.result.transaction_details)
        self.assertEqual(1, len(response.result.transaction_details))

        transaction_details = response.result.transaction_details[0]
        self.assertIsNotNone(transaction_details)
        transaction_info = transaction_details.transaction_info
        self.assertIsNotNone(transaction_info)

        self.assertEqual(transaction_id, transaction_info.transaction_id)
        transaction_amount = transaction_info.transaction_amount
        self.assertIsNotNone(transaction_amount)

        self.assertEqual("USD", transaction_amount.currency_code)
        self.assertEqual("10.00", transaction_amount.value)

if __name__ == "__main__":
    unittest.main()
