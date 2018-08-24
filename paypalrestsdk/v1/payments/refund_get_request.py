# This class was generated on Sat, 07 Apr 2018 16:49:42 UTC by version 0.1.0-dev+2136c8-dirty of Braintree SDK Generator
# refund_get_request.py
# @version 0.1.0-dev+2136c8-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class RefundGetRequest:
    """
    Shows details for a refund, by ID.
    """
    def __init__(self, refund_id):
        self.verb = "GET"
        self.path = "/v1/payments/refund/{refund_id}?".replace("{refund_id}", quote(str(refund_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
