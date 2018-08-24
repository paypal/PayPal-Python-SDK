# This class was generated on Mon, 29 Jan 2018 15:08:24 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# web_profile_update_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebProfileUpdateRequest:
    """
    Updates a web experience profile, by ID. In the JSON request body, specify the profile details. If your request omits any profile parameters, any previously set values for those parameters are removed.
    """
    def __init__(self, profile_id):
        self.verb = "PUT"
        self.path = "/v1/payment-experience/web-profiles/{profile_id}?".replace("{profile_id}", quote(str(profile_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, web_profile):
        self.body = web_profile
        return self
