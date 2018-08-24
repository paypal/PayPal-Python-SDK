# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# search_get_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data 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
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class SearchGetRequest:
    """
    Shows details for a transaction, by transaction date or transaction ID. To filter the transaction that appears in the response, specify one or more optional query parameters.<blockquote><strong>Note:</strong> If you specify query parameters, the `ending_balance` field does not contain a value.</blockquote><br/>To limit, or <em>page</em>, the data that appears in the response, use these query parameters:<table><thead><tr><th>Parameter</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>page</code></td><td>integer</td><td>The zero-relative start index of the entire list of items that are returned in the response. So, the combination of <code>page=1</code> and <code>page_size=20</code> returns the first 20 items.</td></tr><tr><td><code>page_size</code></td><td>integer</td><td>The number of items to return in the response.</td></tr></tbody></table>
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/reporting/transactions?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def balance_affecting_records_only(self, balance_affecting_records_only):
        params = str(balance_affecting_records_only)
        self.path += "balance_affecting_records_only=" + quote(params) + "&"
        return self

    def end_date(self, end_date):
        params = str(end_date)
        self.path += "end_date=" + quote(params) + "&"
        return self

    def fields(self, fields):
        params = str(fields)
        self.path += "fields=" + quote(params) + "&"
        return self

    def page(self, page):
        params = str(page)
        self.path += "page=" + quote(params) + "&"
        return self

    def page_size(self, page_size):
        params = str(page_size)
        self.path += "page_size=" + quote(params) + "&"
        return self

    def payment_instrument_type(self, payment_instrument_type):
        params = str(payment_instrument_type)
        self.path += "payment_instrument_type=" + quote(params) + "&"
        return self

    def start_date(self, start_date):
        params = str(start_date)
        self.path += "start_date=" + quote(params) + "&"
        return self

    def store_id(self, store_id):
        params = str(store_id)
        self.path += "store_id=" + quote(params) + "&"
        return self

    def terminal_id(self, terminal_id):
        params = str(terminal_id)
        self.path += "terminal_id=" + quote(params) + "&"
        return self

    def transaction_amount(self, transaction_amount):
        params = str(transaction_amount)
        self.path += "transaction_amount=" + quote(params) + "&"
        return self

    def transaction_currency(self, transaction_currency):
        params = str(transaction_currency)
        self.path += "transaction_currency=" + quote(params) + "&"
        return self

    def transaction_id(self, transaction_id):
        params = str(transaction_id)
        self.path += "transaction_id=" + quote(params) + "&"
        return self

    def transaction_status(self, transaction_status):
        params = str(transaction_status)
        self.path += "transaction_status=" + quote(params) + "&"
        return self

    def transaction_type(self, transaction_type):
        params = str(transaction_type)
        self.path += "transaction_type=" + quote(params) + "&"
        return self

    
