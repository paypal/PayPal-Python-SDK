# This class was generated on Mon, 29 Jan 2018 15:08:24 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# web_profile_create_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebProfileCreateRequest:
    """
    Creates a web experience profile. In the JSON request body, specify the profile name and details.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/payment-experience/web-profiles/?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, web_profile):
        self.body = web_profile
        return self
