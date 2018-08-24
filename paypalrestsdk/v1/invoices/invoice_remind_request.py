# This class was generated on Mon, 29 Jan 2018 15:08:23 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# invoice_remind_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/6xVwW7bMAy97ysInY0k24AdfCvSDc2GJtlS7LIVKWPRtTpbdCW6nVHk3wfZTho7LYpivQTRk0y+Rz5RD2qOBalYGXvHJqGRo8JYrSJ1Sj5xphTDVsVqRVZ7QGi3yYEwSEZQYk0OcMOVAFrookSwqWF2OoKZbU59XS3m4Oi2Ii+wYV1HYGySV5oA4cqymNQkGFJdAW9uKBGQDAU0pcaSb2L4qt3gtFnuiaDVwJKRA02CJvcjFanvFbl6iQ4LEnJexb8uI3VGqMkN0S/siiG2RMl62IO6qMtQJi/O2GsVqZ/oDG5y6pdvbULpvlHdwUd1vMgIZqc7Ed1XkLKD+8wkWSirJ6sPKh3knDiHdctgEqkfhHph81rFKeaeAnBbGUdaxeIqitTScUlODHkV2yrPt5ftGfLSBtnLmR+U/lhU6FRPTgccS6ICTQ7sYHW+gsN+vop9BxzSf7nySbJusvse00O0T/fEAgZCoQdsKZAu2BFMp3Erw49glkLNFXBhghGNh3JnBkgdF895GnvSwfjQSwk9xTx/TACotSPvG2OjALpwj5wMXDGCRbD1vfEUgS8pMWk9ZCMMuWlZ0nFw7kx1yMo36QKv0e9qMvmYbHJO/txWLNSs29/Ei2N73SJzFopbeHyIw4nWJsTE/Ch3SGJZwFdlyU5Id9nGw3R9f3x6rT8ae0cvmsSyUM8fHTCwRqBMvdH2v/4d8Nsw54RPXLVw6dfC64JckqGVHtknNvvEZ1aH9pKH+4yaWfg4RxIu652z2i51+nbR3ljicy3o5ndf2B47HimDef+WQ6WdidtwypdsPbVxAhypKVsh2w1KhWWZd1nHN74Zkmci5TlJxlrFarlYXaj2wVCxGt+9H7e319jr7h/58cPj67Ad7x/Yz39LSoT0SlAqP2VNKv4wmWzf/QMAAP//
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class InvoiceRemindRequest:
    """
    Sends a reminder to the payer about an invoice, by ID. In the JSON request body, include a `notification` object that defines the subject of the reminder and other details.
    """
    def __init__(self, invoice_id):
        self.verb = "POST"
        self.path = "/v1/invoicing/invoices/{invoice_id}/remind?".replace("{invoice_id}", quote(str(invoice_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, body):
        self.body = body
        return self
