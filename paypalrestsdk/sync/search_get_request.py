# This class was generated on Fri, 26 Jan 2018 14:16:06 CST by version 0.1.0-dev+47ed6e of Braintree SDK Generator
# search_get_request.py
# @version 0.1.0-dev+47ed6e
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

    
