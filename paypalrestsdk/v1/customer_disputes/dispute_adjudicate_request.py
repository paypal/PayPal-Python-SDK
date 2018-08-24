# This class was generated on Sun, 08 Apr 2018 16:12:12 UTC by version 0.1.0-dev+291f3f of Braintree SDK Generator
# dispute_adjudicate_request.py
# @version 0.1.0-dev+291f3f
# @type request
# @data H4sIAAAAAAAC/7yWUW/jRBDH3/kUowWJRnLigrjj8Ft0vVMrDhqaHC9RdZnYk3gv9q7ZGTe1qn53tF4nqROgIKp7S8azu//f/MezflC/YkkqUZnmqhYaYfa5znSKQipSF8Sp05Voa1SipiRSEANClxzBsoGriwi0AdKSkwPJCZZ1Q+5bBuuAqSja3yu8s26kIvVbTa6ZoMOShByrZH4bqUvCjNxx9L115XFsgpL3Yg9q1lQegMVps1aR+h2dxmVBfbBPOlOR+pmaLnxCN8sJri7ArlqGbhWIBW6xvfaxc9iE484jdUOYXZuiUckKCyYf+KPWjjKViKspUhNnK3KiiVVi6qJ4vA05xBI22Wsf74sOXcIpx9JmTY+gC/QpxuDCBl75wcuDZ//Fq3/N2wWeAj9vzF6dtuaTrSW1JfUA/ybh1Lbu2c67p+v+L0bw7dFncWUN05Fz03rJvuBGYJz6A/kU9J/77skOGHZ4udJ/0GYDT4870VZos+GewF3kqK8MoJfka9x12NBRgUIZzC/Hs3fX4ym0S2/P4symHGOl4xyFLPKwfRAPjsBev3xP5Y5WPZoucNozqS2rgvwbjm5NAh9vPoxgZqHEDbVdtKNLsSgin77UJjwpSXKbwVZLDpJrhvnHmyuYUVn5FcOVdSWKUHZ7lotUnMSxWFvwSJOsRtat41zKInar9PWrH88HbdVG8N46qBwNK2dTYtZm7cdqWtRZOHTxzSKCxdkiAjQZLAYLSHN0mPoxOAJPtPCsC9Dc5m+ogZ0vntUa32GSowSbAPclCIyBB4EP/ejDL/ICRc8aF2ras24fOjXvcjab7Gxw3el+4P2leV+IwFHRkx/+n2qf+/IHgdoakKaiZxvl1U9v3nzN1I6H4Q+DCLa5TnNgcnf+PmZA4++ulXWArb3B6NpgudTr2tZcNJC1UpYU+oOpRCM65d3UDG04JYJ5OzZuOoV8ULfdbkcaDbbakFmvTUlGOPZrhzuk47+je48xeKFJ7GfxW2uETHeJKqyqopv28Wduh9ylSPVLaJ9ETa6nMxW+HFSi4rvv4rRmsSW5uLsTOX44fCU8xr1PoOlGV3s97+4rSoWyqaDU/NZmpJLvz88fv/oTAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class DisputeAdjudicateRequest:
    """
    Settles a dispute, by ID, in either the buyer's or seller's favor.
    """
    def __init__(self, dispute_id):
        self.verb = "POST"
        self.path = "/v1/customer/disputes/{dispute_id}/adjudicate?".replace("{dispute_id}", quote(str(dispute_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, body):
        self.body = body
        return self
