from paypalrestsdk.resource import Find, Create, Delete


# == Example
#   credit_card = CreditCard.find("CARD-5BT058015C739554AKE2GCEI")
#   credit_card = CreditCard.new({'type': 'visa'})
#
#   credit_card.create()  # return True or False
class CreditCard(Find, Create, Delete):

    path = "v1/vault/credit-card"

CreditCard.convert_resources['credit_card'] = CreditCard
