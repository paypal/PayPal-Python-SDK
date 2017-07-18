from paypalrestsdk import CreditCard, ResourceNotFound
import logging

logging.basicConfig(level=logging.INFO)

try:
    credit_card = CreditCard.find("CARD-5U686097RY597093SKPL7UNI")
    print("Got CreditCard[%s]" % (credit_card.id))

    credit_card_update_attributes = [{
        "op": "replace",
        "path": "/first_name",
        "value": "Billy"
    }]

    if credit_card.replace(credit_card_update_attributes):
        print("Card [%s] first name changed to %s" %
              (credit_card.id, credit_card.first_name))
    else:
        print(credit_card.error)

except ResourceNotFound as error:
    print("Billing Plan Not Found")
