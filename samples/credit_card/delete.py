from paypalrestsdk import CreditCard
import logging
logging.basicConfig(level=logging.INFO)

credit_card = CreditCard.find("CARD-7LT50814996943336KESEVWA")

if credit_card.delete():
    print("CreditCard deleted")
else:
    print(credit_card.error)
