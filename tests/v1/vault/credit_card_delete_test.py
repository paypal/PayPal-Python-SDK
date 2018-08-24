import unittest

from paypalrestsdk.v1.vault import CreditCardDeleteRequest

from tests.testharness import TestHarness
from tests.v1.vault import create_credit_card

class CreditCardDeleteTest(TestHarness):

    def testCreditCardDeleteTest(self):
        create_response = create_credit_card(self.client)
        self.assertEqual(201, create_response.status_code)

        request = CreditCardDeleteRequest(create_response.result.id)
        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

if __name__ == "__main__":
    unittest.main()
