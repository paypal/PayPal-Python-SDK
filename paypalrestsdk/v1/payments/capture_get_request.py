# This class was generated on Sat, 07 Apr 2018 16:49:42 UTC by version 0.1.0-dev+2136c8-dirty of Braintree SDK Generator
# capture_get_request.py
# @version 0.1.0-dev+2136c8-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class CaptureGetRequest:
    """
    Shows details for a captured payment, by ID.
    """
    def __init__(self, capture_id):
        self.verb = "GET"
        self.path = "/v1/payments/capture/{capture_id}?".replace("{capture_id}", quote(str(capture_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
