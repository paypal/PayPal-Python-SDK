# This class was generated on Sat, 07 Apr 2018 16:49:42 UTC by version 0.1.0-dev+2136c8-dirty of Braintree SDK Generator
# capture_refund_request.py
# @version 0.1.0-dev+2136c8-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class CaptureRefundRequest:
    """
    Refunds a captured payment, by ID. In the JSON request body, include an `amount` object.
    """
    def __init__(self, capture_id):
        self.verb = "POST"
        self.path = "/v1/payments/capture/{capture_id}/refund?".replace("{capture_id}", quote(str(capture_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def paypal_request_id(self, paypal_request_id):
        self.headers["PayPal-Request-Id"] = str(paypal_request_id)

    
    
    def request_body(self, refund_request):
        self.body = refund_request
        return self
