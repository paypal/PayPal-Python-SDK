# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# webhook_delete_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/2SQzU7jMBSF9/MU1llbTWc0K+9QE9SKvwIVG1Qht74lhtQ29g0QVX13ZBIELdtPx77fOTtc6i1B4Y1WtffPI0MNMUGipLSONrD1DgrlJ05CiyEoxaoTs3IEieuWYjfXUW+JKSao+6XElLSheExPfdwes7nm+oDtsOhCdkocrXuExJ2OVq8aOnR9sAYSZ9QN+Jf0oiYxK4XfCK7pS1ywF33J7H4So+76c2OJG9LmyjUd1EY3iTJ4aW0kA8WxJYl59IEiW0pQrm2a/bLPUOL+kwwzSsG7RD/ZxDsmN8SgQ2jsWmfR4il5B4kpc7ggrr3Je1fn1aJCvw4Uite/hfNsN8OjVAx1UrH7nmMPieo90JrJ3LLmNk28Iah/4//7Px8AAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhookDeleteRequest:
    """
    Deletes a webhook, by ID.
    """
    def __init__(self, webhook_id):
        self.verb = "DELETE"
        self.path = "/v1/notifications/webhooks/{webhook_id}?".replace("{webhook_id}", quote(str(webhook_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
