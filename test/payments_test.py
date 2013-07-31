from test_helper import paypal, unittest

class TestPayment(unittest.TestCase):

  def test_create(self):
    payment = paypal.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "credit_card",
        "funding_instruments": [{
          "credit_card": {
            "type": "visa",
            "number": "4417119669820331",
            "expire_month": "11",
            "expire_year": "2018",
            "cvv2": "874",
            "first_name": "Joe",
            "last_name": "Shopper" }}]},
      "transactions": [{
        "item_list": {
          "items": [{
            "name": "item",
            "sku": "item",
            "price": "1.00",
            "currency": "USD",
            "quantity": 1 }]},
        "amount": {
          "total": "1.00",
          "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    self.assertEqual(payment.create(), True)

  def test_validation(self):
    payment = paypal.Payment({})
    self.assertEqual(payment.create(), False)

  def test_all(self):
    payment_histroy = paypal.Payment.all({"count": 1 })
    self.assertEqual(payment_histroy.count, 1)
    self.assertEqual(payment_histroy.payments[0].__class__, paypal.Payment)

    # payment_histroy = paypal.Payment.all({"count": 5 })
    # payment_histroy = paypal.Payment.all({"count": 10 })
    # payment_histroy = paypal.Payment.all({"count": 15 })

  def test_find(self):
    payment_history = paypal.Payment.all({"count": 1 })
    payment_id = payment_history.payments[0]['id']
    payment = paypal.Payment.find(payment_id)
    self.assertEqual(payment.id, payment_id)

  def test_not_found(self):
    self.assertRaises(paypal.ResourceNotFound, paypal.Payment.find, ("PAY-1234"))

  def test_execute(self):
    payment = paypal.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "paypal" },
      "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/" },
      "transactions": [{
        "item_list": {
          "items": [{
            "name": "item",
            "sku": "item",
            "price": "1.00",
            "currency": "USD",
            "quantity": 1 }]},
        "amount": {
          "total": "1.00",
          "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    self.assertEqual(payment.create(), True)
    payment.execute({ 'payer_id': 'HZH2W8NPXUE5W' })

class TestSale(unittest.TestCase):

  def create_sale(self):
    payment = paypal.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "credit_card",
        "funding_instruments": [{
          "credit_card": {
            "type": "visa",
            "number": "4417119669820331",
            "expire_month": "11",
            "expire_year": "2018",
            "cvv2": "874",
            "first_name": "Joe",
            "last_name": "Shopper" }}]},
      "transactions": [{
        "amount": {
          "total": "1.00",
          "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    self.assertEqual(payment.create(), True)
    return payment.transactions[0].related_resources[0].sale
    
  def test_find(self):
    sale = paypal.Sale.find(self.create_sale().id)
    self.assertEqual(sale.__class__, paypal.Sale)

  def test_refund(self):
    sale   = paypal.Sale.find(self.create_sale().id)
    refund = sale.refund({ "amount": { "total": "0.01", "currency": "USD" } })
    self.assertEqual(refund.success(), True)

class TestRefund(unittest.TestCase):

  def test_find(self):
    refund = paypal.Refund.find("5C377143F71265517")
    self.assertEqual(refund.__class__, paypal.Refund)


class TestAuthorization(unittest.TestCase):

  def create_authorization(self):
    payment = paypal.Payment({
      "intent": "authorize",
      "payer": {
        "payment_method": "credit_card",
        "funding_instruments": [{
          "credit_card": {
            "type": "visa",
            "number": "4417119669820331",
            "expire_month": "11",
            "expire_year": "2018",
            "cvv2": "874",
            "first_name": "Joe",
            "last_name": "Shopper" }}]},
      "transactions": [{
        "item_list": {
          "items": [{
            "name": "item",
            "sku": "item",
            "price": "1.00",
            "currency": "USD",
            "quantity": 1 }]},
        "amount": {
          "total": "1.00",
          "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    self.assertEqual(payment.create(), True)
    return payment.transactions[0].related_resources[0].authorization

  def test_find(self):
    authorization = paypal.Authorization.find(self.create_authorization().id)
    self.assertEqual(authorization.__class__, paypal.Authorization)


  def test_capture(self):
    authorization = self.create_authorization()
    capture = authorization.capture({ "amount": { "currency": "USD", "total": "1.00" } })
    self.assertEqual(capture.success(), True)

  def test_void(self):
    authorization = self.create_authorization()
    self.assertEqual(authorization.void(), True)

  def test_capture_find(self):
    authorization = self.create_authorization()
    capture = authorization.capture({ "amount": { "currency": "USD", "total": "1.00" } })
    self.assertEqual(capture.success(), True)

    capture = paypal.Capture.find(capture.id)
    self.assertEqual(capture.__class__, paypal.Capture)

  def test_reauthorize(self):
    authorization = paypal.Authorization.find("7GH53639GA425732B")
    authorization.amount = {
      "currency": "USD",
      "total": "7.00" }
    self.assertEqual(authorization.reauthorize(), False)

  def test_capture_refund(self):
    authorization = self.create_authorization()
    capture = authorization.capture({ "amount": { "currency": "USD", "total": "1.00" } })
    self.assertEqual(capture.success(), True)

    refund = capture.refund({ "amount": { "currency": "USD", "total": "1.00" } })
    self.assertEqual(refund.success(), True)
    self.assertEqual(refund.__class__, paypal.Refund)

