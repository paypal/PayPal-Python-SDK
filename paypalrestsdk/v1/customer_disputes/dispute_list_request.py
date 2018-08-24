# This class was generated on Sun, 08 Apr 2018 16:12:12 UTC by version 0.1.0-dev+291f3f of Braintree SDK Generator
# dispute_list_request.py
# @version 0.1.0-dev+291f3f
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class DisputeListRequest:
    """
    Lists disputes. To filter the disputes in the response, specify one or more optional query parameters. To limit the number of disputes in the response, specify the <code>page_size</code> query parameter.
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/customer/disputes?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def dispute_state(self, dispute_state):
        params = str(dispute_state)
        self.path += "dispute_state=" + quote(params) + "&"
        return self

    def disputed_transaction_id(self, disputed_transaction_id):
        params = str(disputed_transaction_id)
        self.path += "disputed_transaction_id=" + quote(params) + "&"
        return self

    def next_page_token(self, next_page_token):
        params = str(next_page_token)
        self.path += "next_page_token=" + quote(params) + "&"
        return self

    def page_size(self, page_size):
        params = str(page_size)
        self.path += "page_size=" + quote(params) + "&"
        return self

    def start_time(self, start_time):
        params = str(start_time)
        self.path += "start_time=" + quote(params) + "&"
        return self

    def total_required(self, total_required):
        params = str(total_required)
        self.path += "total_required=" + quote(params) + "&"
        return self

    
