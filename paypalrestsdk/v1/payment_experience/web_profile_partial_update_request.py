# This class was generated on Mon, 29 Jan 2018 15:08:24 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# web_profile_partial_update_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/7SVUU/bQAzH3/cpLD8fLZumPeQNwSbYNOgG2suEwE1ccii9O3wOJUL97tMlaUtTNMamvbX/cxz//Hd8j3hKc8YMFzzdC+JntuJRIFFL1V4dClJGg0ccc7FBrXeY4aQ7rpo+IALBgqfAD4HFsssZ+kwGpg2cHI3gxIGWDJ/Pz05B+K7mqDD1RWMgBs7trAGCQJqX4Ke3nKtpwwNpCX7W/e4yQuVzSnWAeuheb4BcAQSOF3BPVc0jNPitZmkmJDRnZYmY/bw0eMxUsAzVT17mQ21CWm5pj3jRhNSnqGLdDRr8QWJpWnHfv76+K1ugwS/c9PJO8y5KhpOjIZV6CKuu9liJ4kCEmu7F+wa/MxVnrmowm1EVOQl3tRUuMFOp2eBEfGBRyxEzV1fV8rKL4ahdkjVFa8QkNfwZkiRf9S5twQxPtskOHFCqN7G1+Z8aGhMihVA1K1BYDY96EI6+lpzjAPrDb6F74Sn1yz7NxM+3oHphwNITeOuUJZWY3FrPnu3GWUluWKHweT1np5BSwaK0eZmemPt7bsO6oYRV4TDz0urXKeIaUvVt2lc5/gx8a7l5sQM+bPG3f3dndF1VQsn9PFT8ypn8+wrTdz8cvPIPPKIXHSLd+LOCagP/lwnd9O8itjOxxbhSdq1oT9bfzwiSdi08mB4oPEdwXtsFa4WBNuvwn4kulykqBu8id3mSbPDQO2XXrxdMBdrOgfFt9A4NHquGr6ylL9LNcXBxeIzdesUMx/dvx4Ga5Mze5vIYP7mK4vhxs1iXaPDjQ+BcuThX0joe+oIxe7f/fvnmFwAAAP//
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebProfilePartialUpdateRequest:
    """
    Partially-updates a web experience profile, by ID. In the JSON request body, specify a patch object, the path of the profile location to update, and a new value.
    """
    def __init__(self, profile_id):
        self.verb = "PATCH"
        self.path = "/v1/payment-experience/web-profiles/{profile_id}?".replace("{profile_id}", quote(str(profile_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, patch_request):
        self.body = patch_request
        return self
