# CreateCreditCard Sample
# Using the 'vault' API, you can store a
# Credit Card securely on PayPal. You can
# use a saved Credit Card to process
# a payment in the future.
# The following code demonstrates how
# can save a Credit Card on PayPal using
# the Vault API.
# API used: POST /v1/vault/credit-cards
from paypalrestsdk import CreditCard
import logging
logging.basicConfig(level=logging.INFO)

credit_card = CreditCard({
    # CreditCard
    # A resource representing a credit card that can be
    # used to fund a payment.
    "type": "visa",
    "number": "4417119669820331",
    "expire_month": "11",
    "expire_year": "2018",
    "cvv2": "874",
    "first_name": "Joe",
    "last_name": "Shopper",

    # Address
    # Base Address object used as shipping or billing
    # address in a payment. [Optional]
    "billing_address": {
        "line1": "52 N Main ST",
        "city": "Johnstown",
        "state": "OH",
        "postal_code": "43210",
        "country_code": "US"}})

# Make API call & get response status
# Save
# Creates the credit card as a resource
# in the PayPal vault.
if credit_card.create():
    print("CreditCard[%s] created successfully" % (credit_card.id))
else:
    print("Error while creating CreditCard:")
    print(credit_card.error)
