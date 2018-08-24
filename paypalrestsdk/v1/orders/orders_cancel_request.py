# This class was generated on Mon, 29 Jan 2018 15:08:24 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# orders_cancel_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/2SSTY/TMBCG7/yK0ZytZkGcfKuaoF3xsaFEe0ErOo1nicGxw3iCiKr+d5RkEaVcn3mVzPuMT/iBekaLSRxL3rQUWw5osOTcih/Up4gWdwvOQBGWoIHjBHelAYoOHAdWzqAdr9MNNAlaCgG08xl61i4583cOWUnHDP2YFY4McNjtq21TlQdIAodtXe/vH6rysEGDH0eWqSahnpUlo/38aPCWybFc0zdJ+mtWk3b/sBM20zAXzio+fkWDDySejoEvRXzxDg2+5ekZ/iek6RjuSkhPF610Lj17mvfeitC0/urG4J7J3ccwoX2ikHkGP0Yv7NCqjGywljSwqOeMNo4hnB/XDGddPzLDGeUhxcyXbJeicnyOIQ1D8C3Naxbfcopo8FZ1eL/cAC2W1buqqXA1gxaLny+LtuP2exq1WB9Bcfrj4IwGq18Dt8ru03KzXXKM9tXN6/OL3wAAAP//
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class OrdersCancelRequest:
    """
    Cancels an order, by ID, and deletes the order. To call this method, the order status must be  `CREATED` or `APPROVED`.
    """
    def __init__(self, order_id):
        self.verb = "DELETE"
        self.path = "/v1/checkout/orders/{order_id}?".replace("{order_id}", quote(str(order_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
