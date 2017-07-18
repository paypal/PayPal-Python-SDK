# GetCreditCard Sample
# This sample code demonstrates how you
# retrieve a previously saved
# Credit Card using the 'vault' API.
# API used: GET /v1/vault/credit-cards/{id}
from paypalrestsdk import CreditCard, ResourceNotFound
import logging
logging.basicConfig(level=logging.INFO)

try:
    # Retrieve the CreditCard  by calling the
    # static `find` method on the CreditCard class,
    # and pass CreditCard ID
    credit_card = CreditCard.find("CARD-5BT058015C739554AKE2GCEI")
    print("Got CreditCard[%s]" % (credit_card.id))

except ResourceNotFound as error:
    print("CreditCard Not Found")
