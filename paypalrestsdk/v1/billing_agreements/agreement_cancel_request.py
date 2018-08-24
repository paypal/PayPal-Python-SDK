# This class was generated on Mon, 29 Jan 2018 15:08:22 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# agreement_cancel_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/6RUX2/TMBB/51Oc7tksA/GUt2kFrSDWQite0NRd4mvjybUz+wJEVb87chKyNZWGEE+Vf73z/f6cc8Bb2jPmSLvAvGcnFyW5ki0qnHEsg6nFeIc5XndwBILCWGvcDsYWBUUL89kFzB1IxfBxtbiFwI8NR4HC61aBcaVtNAM5uB/7NlFIeKOHOT7cgy8euBT4aaRKtb6bThacFwapSKCvLjh2owJT9A62PnTHnrul1AXkdAeO84D2vkk/TkPZhMCubC9Q4ZeGQ7ukQHsWDhHz73cKb5g0hyn6wYf9FFuSVCfYAddtnUyNEozbocJvFAwVlqdmb4xGhZ+4Hf44c31dMcxn4LcTJeIHrYn/VQjU9iMvFX5l0gtnW8y3ZCMn4LExgTXmEhpWuAy+5iCGI+ausfZ419dwlP6Skf/VOG+VkoLZmNRLmqapnih8sexU+xXop/MfC/rcBLruM1/+yY0BeG7H36NLi3giaADOY5us5lN2PfWyIrfj/yXc53dMVbH2LnJ/T4IVXnsn7IZQkeramrJ7GtlD9A4V3ojUn1kqrzHH5WK1xn6bMcfsx5uspjYRjtnw4l+PGmJ2eL7Dx2z8aLz/VXMprNPCNPHaa8b87eW746vfAAAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class AgreementCancelRequest:
    """
    Cancels a billing agreement, by ID. In the JSON request body, include an `agreement_state_descriptor` object with an optional note that describes the reason for the cancellation and the agreement amount and currency.
    """
    def __init__(self, agreement_id):
        self.verb = "POST"
        self.path = "/v1/payments/billing-agreements/{agreement_id}/cancel?".replace("{agreement_id}", quote(str(agreement_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, agreement_state_descriptor):
        self.body = agreement_state_descriptor
        return self
