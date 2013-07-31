from paypalrestsdk.resource import List, Find, Create, Post

# == Example
#  payment_histroy = Payment.all({"count": 5})
#  payment = Payment.find("PAY-1234")
#  payment = Payment.new({"intent": "sale"})
#
#  payment.create()     # return True or False
#  payment.execute({"payer_id": 1234})  # return True or False
class Payment(List, Find, Create, Post):

  path = "v1/payments/payment"

  def execute(self, attributes):
    return self.post('execute', attributes, self)

Payment.convert_resources['payments'] = Payment
Payment.convert_resources['payment']  = Payment

# == Example
#  sale = Sale.find("98765432")
#
#  refund = sale.refund({"amount": {"total": "1.00", "currency": "USD"}})
#  refund.success()   # return True or False
class Sale(Find, Post):

  path = "v1/payments/sale"

  def refund(self, attributes):
    return self.post('refund', attributes, Refund)

Sale.convert_resources['sales'] = Sale
Sale.convert_resources['sale']  = Sale


# == Example
#  refund = Refund.find("12345678")
class Refund(Find):

  path = "v1/payments/refund"

Refund.convert_resources['refund'] = Refund

# == Example
#   authorization = Authorization.find("")
#   capture = authorization.capture({ "amount": { "currency": "USD", "total": "1.00" } })
#   authorization.void() # return True or False
class Authorization(Find, Post):

  path = "v1/payments/authorization"

  def capture(self, attributes):
    return self.post('capture', attributes, Capture)

  def void(self):
    return self.post('void', {}, self)

  def reauthorize(self):
    return self.post('reauthorize', self, self)

Authorization.convert_resources['authorization'] = Authorization

# == Example
#   capture = Capture.find("")
#   refund = capture.refund({ "amount": { "currency": "USD", "total": "1.00" })
class Capture(Find, Post):

  path = "v1/payments/capture"

  def refund(self, attributes):
    return self.post('refund', attributes, Refund)

Capture.convert_resources['capture'] = Capture
