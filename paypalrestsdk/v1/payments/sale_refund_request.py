# This class was generated on Sat, 07 Apr 2018 16:49:42 UTC by version 0.1.0-dev+2136c8-dirty of Braintree SDK Generator
# sale_refund_request.py
# @version 0.1.0-dev+2136c8-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class SaleRefundRequest:
    """
    Refunds a sale, by ID. For a full refund, do not include the `amount` object in the JSON request body. For a partial refund, include an `amount` object in the JSON request body.
    """
    def __init__(self, sale_id):
        self.verb = "POST"
        self.path = "/v1/payments/sale/{sale_id}/refund?".replace("{sale_id}", quote(str(sale_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def paypal_request_id(self, paypal_request_id):
        self.headers["PayPal-Request-Id"] = str(paypal_request_id)

    
    
    def request_body(self, refund_request):
        self.body = refund_request
        return self
