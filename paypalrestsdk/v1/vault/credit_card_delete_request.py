# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# credit_card_delete_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/2yRzW4aMRDH730Ka84uS3v0rWK3AvWLtiiXCKFhPWQdGdsZz6KsEO8emeUAJNefZzz/jyP8xj2BgZbJOvncItuJJU9CoKGm3LJL4mIAA/UZZ4XqgL0XsmpcUmVJq+2gFvUENPztiYclMu5JiDOYx7WGOaElvqffI+/v2RKlu2FHWA2paMzCLjyBhgdkh1tPN9o3RcbGWdDwg4bL0zsTq47UolZxp6Sjj4woiWoMoHj5xozDeH6q4R+h/RP8AGaHPlMBL71jsmCEe9Kw5JiIxVEGE3rvT+txhrKMnxRYUE4xZLpmsxiEwmUMMCXvWiyiq+ccA2iYi6RfJF20pYvmZ7NqYEwLDFSHL9XZTHVVZK6Ot9GcQEPzmqgVsv8Fpc+zaAnM1+n09OkNAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class CreditCardDeleteRequest:
    """
    Deletes a vaulted credit card, by ID.
    """
    def __init__(self, credit_card_id):
        self.verb = "DELETE"
        self.path = "/v1/vault/credit-cards/{credit_card_id}?".replace("{credit_card_id}", quote(str(credit_card_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
