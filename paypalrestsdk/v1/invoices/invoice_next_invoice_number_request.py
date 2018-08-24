# This class was generated on Mon, 29 Jan 2018 15:08:23 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# invoice_next_invoice_number_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/6SST2/UMBDF73wKa87ZP3DMDZU/RQi60BUXVFXT5LUxSsZmPFk1qva7I+OwVYO40FMyTzOen9/zA33mAVSTl0PwDdaCe7uei2sZhxsoVfQGqVEfzQehmt5DoGxIzjq4POHmCVcmnHVszifHB/Y93/RwFn43D9CmY7E1VfRlhE47Vh5g0ET196uKzsEtdKm+CzostR1bt9S+4ueIZPspgmoZ+z5LKQZJKNoDlS99eAJMFX1j9Zl09oMq+ojpsXjqAFX0WpWnctg2b+H2QvqJ6lvuEwqJV7QnYachQs0jo54wkqmXu7/Xn7AeIf4Rxv6/I3D7zqc/7blztLDy0igGiKF1txqGMhKSOUUDWa5ZP9OJnNHx6ljRWRCDzMkRx9j7hvMVNz9SEKro3Cx+gnWhpZp2F5d7Kk+AatocXm4Klpe7+Q9pk11ZzdXq5N7b+4jG0F4a25jOQguqX223xxe/AAAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class InvoiceNextInvoiceNumberRequest:
    """
    Generates the next invoice number that is available to the merchant.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/invoicing/invoices/next-invoice-number?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
