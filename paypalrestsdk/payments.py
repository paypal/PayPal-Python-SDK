from paypalrestsdk.resource import List, Find, Create, Post, Update, Replace, Resource
from paypalrestsdk.api import default as default_api
import paypalrestsdk.util as util
from paypalrestsdk import exceptions


class Payment(List, Find, Create, Post, Replace):
    """Payment class wrapping the REST v1/payments/payment endpoint

    Usage::

        >>> payment_history = Payment.all({"count": 5})
        >>> payment = Payment.find("<PAYMENT_ID>")
        >>> payment = Payment.new({"intent": "sale"})
        >>> payment.create()     # return True or False
        >>> payment.execute({"payer_id": 1234})  # return True or False
    """
    path = "v1/payments/payment"

    def execute(self, attributes):
        return self.post('execute', attributes, self)

Payment.convert_resources['payments'] = Payment
Payment.convert_resources['payment'] = Payment


class BillingPlan(List, Create, Find, Replace):
    """Merchants can create subscription payments i.e. planned sets of
    future recurring payments at periodic intervals. Billing Plans specify
    number of payments, their frequency and other details. Acts as a template
    for BillingAgreement, one BillingPlan can be used to create multiple
    agreements.
    Wraps the v1/payments/billing-plans endpoint

    https://developer.paypal.com/webapps/developer/docs/integration/direct/create-billing-plan/

    Usage::

        >>> billing_plans = BillingPlan.all({'status': CREATED})
    """
    path = "v1/payments/billing-plans"

    def activate(self):
        """Activate a billing plan, wraps billing plan replace."""
        billing_plan_update_attributes = [{
            "op": "replace",
            "path": "/",
            "value": {
                "state": "ACTIVE"
            }
        }]

        return self.replace(billing_plan_update_attributes)

    def inactivate(self):
        """Inactivate a billing plan, wraps billing plan replace."""
        billing_plan_update_attributes = [{
            "op": "replace",
            "path": "/",
            "value": {
                "state": "INACTIVE"
            }
        }]

        return self.replace(billing_plan_update_attributes)

BillingPlan.convert_resources['billingplan'] = BillingPlan
BillingPlan.convert_resources['billingplans'] = BillingPlan


class BillingAgreement(Create, Find, Replace, Post):
    """After billing plan is created and activated, the billing agreement
    resource can be used to have customers agree to subscribe to plan.
    Wraps the v1/payments/billing-agreements endpoint

    https://developer.paypal.com/webapps/developer/docs/integration/direct/create-billing-agreement/

    Usage::

        >>> billing_agreement = BillingAgreement.find("<AGREEMENT_ID>")
    """
    path = "v1/payments/billing-agreements"

    def suspend(self, attributes):
        return self.post('suspend', attributes, self)

    def cancel(self, attributes):
        return self.post('cancel', attributes, self)

    def reactivate(self, attributes):
        return self.post('re-activate', attributes, self)

    def bill_balance(self, attributes):
        return self.post('bill-balance', attributes, self)

    def set_balance(self, attributes):
        return self.post('set-balance', attributes, self)

    @classmethod
    def execute(cls, payment_token, params=None, api=None):
        api = api or default_api()
        params = params or {}

        url = util.join_url(cls.path, payment_token, 'agreement-execute')

        return Resource(api.post(url, params), api=api)

    def search_transactions(self, start_date, end_date, api=None):
        if not start_date or not end_date:
            raise exceptions.MissingParam("Search transactions needs valid start_date and end_date.")
        api = api or default_api()

        # Construct url similar to
        # /billing-agreements/I-HT38K76XPMGJ/transactions?start-date=2014-04-13&end-date=2014-04-30
        endpoint = util.join_url(self.path, str(self['id']), 'transactions')
        date_range = [('start_date', start_date), ('end_date', end_date)]
        url = util.join_url_params(endpoint, date_range)

        return Resource(self.api.get(url), api=api)

BillingAgreement.convert_resources['billingagreement'] = BillingAgreement
BillingAgreement.convert_resources['billingagreements'] = BillingAgreement


class Sale(Find, Post):
    """Sale class wrapping the REST v1/payments/sale endpoint

    Usage::

        >>> sale = Sale.find("<SALE_ID>")
        >>> refund = sale.refund({"amount": {"total": "1.00", "currency": "USD"}})
        >>> refund.success()   # return True or False
    """
    path = "v1/payments/sale"

    def refund(self, attributes):
        return self.post('refund', attributes, Refund)

Sale.convert_resources['sales'] = Sale
Sale.convert_resources['sale'] = Sale


class Refund(Find):
    """Get details for a refund on direct or captured payment

    Usage::

        >>> refund = Refund.find("<REFUND_ID")
    """
    path = "v1/payments/refund"

Refund.convert_resources['refund'] = Refund


class Authorization(Find, Post):
    """Enables looking up, voiding and capturing authorization and reauthorize payments

    Helpful links::
    https://developer.paypal.com/docs/api/#authorizations
    https://developer.paypal.com/docs/integration/direct/capture-payment/#authorize-the-payment

    Usage::

        >>> authorization = Authorization.find("<AUTHORIZATION_ID>")
        >>> capture = authorization.capture({ "amount": { "currency": "USD", "total": "1.00" } })
        >>> authorization.void() # return True or False
    """
    path = "v1/payments/authorization"

    def capture(self, attributes):
        return self.post('capture', attributes, Capture)

    def void(self):
        return self.post('void', {}, self)

    def reauthorize(self):
        return self.post('reauthorize', self, self)

Authorization.convert_resources['authorization'] = Authorization


class Capture(Find, Post):
    """Look up and refund captured payments and orders, wraps v1/payments/capture

    Usage::

        >>> capture = Capture.find("<CAPTURE_ID>")
        >>> refund = capture.refund({ "amount": { "currency": "USD", "total": "1.00" }})
    """
    path = "v1/payments/capture"

    def refund(self, attributes):
        return self.post('refund', attributes, Refund)


Capture.convert_resources['capture'] = Capture


class Order(Find, Post):
    """Enables looking up, voiding, authorizing and capturing a paypal order which
    is a payment created with intent order. This indicates buyer consent for a purchase
    and does not place funds on hold.

    Usage::
        >>> order = Order.find("<ORDER_ID>")
        >>> order.void()
    """
    path = "v1/payments/orders"

    def capture(self, attributes):
        return self.post('capture', attributes, Order)

    def void(self):
        return self.post('do-void', {}, self)

    def authorize(self, attributes):
        return self.post('authorize', attributes, self)


Order.convert_resources['order'] = Order


class Payout(Create, Find):
    """

    Usage::
        >>> payout = Payout.find("<PAYOUT_ID>")
    """
    path = '/v1/payments/payouts'

    def create(self, sync_mode=False, **kwargs):
        """Creates a payout resource
        """
        if sync_mode:
            self.path = "/v1/payments/payouts?sync_mode=true"
        return super(Payout, self).create(**kwargs)


Payout.convert_resources['payout'] = Payout


class PayoutItem(Find, Post):
    """

    Usage::
        >>> payout = Payout.find("<PAYOUT_ID>")
    """
    path = '/v1/payments/payouts-item'

    def cancel(self):
        return self.post('cancel', {}, self, fieldname='payout_item_id')


PayoutItem.convert_resources['payoutItem'] = PayoutItem
PayoutItem.convert_resources['payoutitem'] = PayoutItem
PayoutItem.convert_resources['payout-item'] = PayoutItem
