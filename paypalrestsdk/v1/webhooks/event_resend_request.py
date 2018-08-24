# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# event_resend_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/8yXXVPjNhfH759PcUZPL2DGselS6G7uMgs7ZLotNGR7wzDkxD6JtdiSKx0TXIbv3pFlBxzzsi+U9tJHsnR+5y/9Jd2I3zAnMRR0RYpDQ5ZUIgJxQDY2smCplRiKSR22gLCiear1JdTdQWmWCxmj6xbAvILxQQgjVUFBKpFq2elgAQ25CNSzcCgC8XtJpjpBgzkxGSuGZ+eBOCJMyGxGP2iTb8ZOkNNO7EZMq8LhWDZSLUUg/kAjcZ7RfcwL6RB/oaoJ9ninKcH4APQCOKUnmIG1h0kczMgYrPz8O4GYECbHKqvEcIGZJRf4s5SGEjFkU1IgTowuyLAkK4aqzLLbc9+HLPtB1jCH9cSTVpuHkAZr5e6wNhq+XdKvYWsC9+GeV6VJ4UImtkPQjXcBRgrQJeVUahEwjnWpGMYHdiPp/a9N2ity63rZQitLD2nSJ3l6XY2eKPY/X+XYEDJdsMypk2Y33t8JCTIBqgRcD1ilpJ7bFiu04EdNApAKzsaKySjijbEW2uTI51spc2GHUcRaZzaUxItQm2WUcp5FZhHv7u6++7+l2I092Av3t7+3VrW4wReaBbtOvX3Vhvvl8vXgFBnYyOWSDCXPFOxVea7IWJdtH+mu5TGqpofT9D7Rv8CyYeEy+WYTf+GEP0p1CfcygeP5Z4ofsIpMqsuu3bWRx43O+PNhYChzmwvOjkbTw+PRKdS/nm9FiY5thIWMUmTSaAd1w/b3uuHz5pIaWnRgmkBfk1jnRUZMwGiWxPBp8jGEqYYcL6mWqoWLMcsC130ulW/JiVOdwEpyCpxKW2N7h/k0GQNTXrhfv9RX9vd+3tkOYazirEz8DLMfZgHMtmZBbVKz7RnEKRqM3f3CDQuFoUFhdEzWSrUMwRHNHOsMpK2HuKQKWlkcq1ZrP6jFAFyXwDN6HgRbzq3TV3EdfqWN5GvakW4d6ot3NJ2etDKYZnZ3C3pQvFciMJR10vff/dzPXPl9gvXdrSro2SWy9+7t2/XR89N2AKtUxilYMldkAS2gcibjVgbW8nqhS4X5XC5LXdqsgqROZU5+fVjKUbGMbWtN7rcQTongrDaPSZOhvctutVqFEhXWuaG1cqlyUmwj9++gRdr8DK8dxsucluf3hNCPOJohq0sT04Ya62BfkrbxP3lctsn1bwCbLX0whTm1+q4h273B+tHT09O+EqAt8xxN1UG7i21eXZuWZjX7s82te17fDjoawQdtgK7ROV0AsxEUWLk1C1hyqo38q3dVDGcvtFDFe62YVPOMElgUWZNV9NnW95sj5uJX73JDcXJ8OhX+MSmGIrr6Meo8W6NGJzuoKW100z4ib6P14+rwuqCYKTll5NK+1wmJ4ZudN7f/+xsAAP//
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class EventResendRequest:
    """
    Resends a webhook event notification, by ID. Any pending notifications are not resent.
    """
    def __init__(self, event_id):
        self.verb = "POST"
        self.path = "/v1/notifications/webhooks-events/{event_id}/resend?".replace("{event_id}", quote(str(event_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, event_resend):
        self.body = event_resend
        return self
