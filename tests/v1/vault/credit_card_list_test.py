import unittest

from paypalrestsdk.v1.vault import CreditCardListRequest

from tests.testharness import TestHarness
from tests.v1.vault import create_credit_card

class CreditCardListTest(TestHarness):

    def testCreditCardListTest(self):
        create_response = create_credit_card(self.client)
        self.assertEqual(201, create_response.status_code)

        list_request = CreditCardListRequest()
        list_response = self.client.execute(list_request)
        self.assertEqual(200, list_response.status_code)
        self.assertIsNotNone(list_response.result)

        credit_card_list = list_response.result.items

        found_credit_card = False
        for credit_card in credit_card_list:
            if credit_card.id == create_response.result.id:
                found_credit_card = True
                self.assertEqual(credit_card.first_name, create_response.result.first_name)
                self.assertEqual(credit_card.last_name, create_response.result.last_name)
                self.assertEqual(credit_card.billing_address.city, create_response.result.billing_address.city)
        self.assertTrue(found_credit_card)

if __name__ == "__main__":
    unittest.main()
