# This class was generated on Sat, 07 Apr 2018 16:49:42 UTC by version 0.1.0-dev+2136c8-dirty of Braintree SDK Generator
# authorization_capture_request.py
# @version 0.1.0-dev+2136c8-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class AuthorizationCaptureRequest:
    """
    Captures and processes an authorization, by ID. The original payment call must specify an intent of `authorize`.
    """
    def __init__(self, authorization_id):
        self.verb = "POST"
        self.path = "/v1/payments/authorization/{authorization_id}/capture?".replace("{authorization_id}", quote(str(authorization_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, capture):
        self.body = capture
        return self
