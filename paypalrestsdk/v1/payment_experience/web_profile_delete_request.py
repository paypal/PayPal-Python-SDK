# This class was generated on Mon, 29 Jan 2018 15:08:24 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# web_profile_delete_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/2SRT4/TMBDF73wKa87eTeHoG9oE7Yp/BSouaIWc+JUYObYZT9hGVb87Colo6V5/Gnt+896RPtgBZOgJ7U3mtPcBtw4BAtJUo3Tss/gUyVD9Fxdl1RNahUMGe8QOan2nVTuph/qWNH0awdPWsh0g4ELm26Ome1gHvqZvEg/XbGul/48daTflWbMI+/iDNH217G0bsOqvCt+9I01vMa342Q27HuqhVmmvpP8nriSp5ebZ/TWznZZ1G02fYd3HGCYyexsKZvBr9AxHRniEpi2nDBaPQiaOIZwelxkUWT6Z4YxKTrHgkt2lKIjrGNmcg+/sLFr9LCmSpnuR/B7SJzfH37xrdg0t6ZCh6vfLKttpQJSbcxnVRZGlOp5zOZGm5pDRCdwXsTKWu+RA5tVmc3rxBwAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebProfileDeleteRequest:
    """
    Deletes a web experience profile, by ID.
    """
    def __init__(self, profile_id):
        self.verb = "DELETE"
        self.path = "/v1/payment-experience/web-profiles/{profile_id}?".replace("{profile_id}", quote(str(profile_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
