# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# credit_card_create_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class CreditCardCreateRequest:
    """
    Stores credit card details in the PayPal vault. To use the vaulted card to make a payment, specify this ID as the `credit_card_id` in a [`credit_card_token`](/docs/api/payments/#definition-credit_card_token) object. If you include a `payer_id` when you store the credit card, you must also include that ID as the `external_customer_id` in the `credit_card_token` object.<br/>You can also use the ID of the vaulted credit card to show details for, update, or delete the vaulted card.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/vault/credit-cards?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, credit_card):
        self.body = credit_card
        return self
