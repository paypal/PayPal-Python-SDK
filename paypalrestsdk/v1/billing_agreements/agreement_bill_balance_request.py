# This class was generated on Mon, 29 Jan 2018 15:08:22 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# agreement_bill_balance_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/6RUTW/TQBC98ytGc97WBXHyLTSgBkQTSMQFVdXYO4kXbXbd3TFgRfnvaG03H45UhDhFeX4z896bsXd4T1vGHGkTmLfs5Low1l4VZMmVjAqnHMtgajHeYY7vjLURpGIYGLD2AcjBoV5B0cJseg0z1/E+Luf3EPip4ShQeN0qMK60jeZU5rvGZMF5YZCKBHQ3sOB+TGCK3nVTuqnGWuM2QGWqA3K6gw/Tgba+ST9OQ9mEwK5sr1Hhl4ZDu6BAWxYOEfPvDwrvmDSHMfrBh+0YW5BUZ9gOV22dcosSjNugwm8UDBWWx3k+Go0KP3E7PLiIdFUxzKbg1yMnyfKvypQViO98n8aePE1CoLaXcaPwK5OeO9tiviYbOQFPjQmsMZfQsMJF8DUHMRwxd421+4eew1H6JgdPk4OGpZAwPOv14SWfMXEf9Sn36PpF2nkeE9DH/8+x9LsU6KovsvqnNAbgNI6/rzOd55mhAbhc5ehgj/vspZcVuQ3/r+B+f/vEirV3kfs+CVZ4652wG5aKVNfWlJQUZj+id6jwTqT+zFJ5jTku5ssV9heOOWY/X2c1tUlwzIaX7ergIWa707veZ6NvxfvfNZfCOp1NE2+9Zszf3Lzdv/oDAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class AgreementBillBalanceRequest:
    """
    Bills the balance for an agreement, by ID. In the JSON request body, include an optional note that describes the reason for the billing action and the agreement amount and currency.
    """
    def __init__(self, agreement_id):
        self.verb = "POST"
        self.path = "/v1/payments/billing-agreements/{agreement_id}/bill-balance?".replace("{agreement_id}", quote(str(agreement_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, agreement_state_descriptor):
        self.body = agreement_state_descriptor
        return self
