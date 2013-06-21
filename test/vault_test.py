from test_helper import paypal, unittest

class TestCreditCard(unittest.TestCase):

  credit_card_attributes = {
      "type": "visa",
      "number": "4417119669820331",
      "expire_month": "11",
      "expire_year": "2018",
      "cvv2": "874",
      "first_name": "Joe",
      "last_name": "Shopper" }

  def test_create_and_find(self):
    credit_card = paypal.CreditCard(self.credit_card_attributes)
    self.assertEqual(credit_card.create(), True)

    credit_card = paypal.CreditCard.find(credit_card.id)
    self.assertEqual(credit_card.__class__, paypal.CreditCard)

  def test_delete(self):
    credit_card = paypal.CreditCard(self.credit_card_attributes)
    self.assertEqual(credit_card.create(), True)
    self.assertEqual(credit_card.delete(), True)

  def test_duplicate_request_id(self):
    credit_card = paypal.CreditCard(self.credit_card_attributes)
    self.assertEqual(credit_card.create(), True)

    new_credit_card = paypal.CreditCard(self.credit_card_attributes)
    new_credit_card.request_id = credit_card.request_id
    self.assertEqual(new_credit_card.create(), True)

    self.assertEqual(new_credit_card.id, credit_card.id)
    self.assertEqual(new_credit_card.request_id, credit_card.request_id)

