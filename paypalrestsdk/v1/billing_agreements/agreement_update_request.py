# This class was generated on Mon, 29 Jan 2018 15:08:22 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# agreement_update_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/7SVQW8TPxDF7/9PMZqz/0nhwGFvVQNqQbSBFi6oaifrSdaVYxt7trCq8t2Rvdu02SBKERz3eTx+P7+Jc4entGaskFaRec1OJm3QJIwKZ5zqaIIY77DCT0VOoFnI2AR+CQQLY61xK9juVrDo4GQ2gdlQZlxtW80gDYN+aKggNSaEslfryCkpSEJRIJ+igJyG5MG7CSr80HLs5hRpzcIxYfXlUuExk+Y4Vt/4uB5rc5JmR7vDiy5k6CTRuBUq/EzR0MLy+DKujEaF77gbFvZu5aJhOJnly8iA230gHvp7zP4PY6SuP/JA4UcmfeZsh9WSbOIsfG1NZI2VxJYVzqMPHMVwwsq11m4u+xpO0jfZ+n97fnYKc5K62WcIWb6K/b4diPHKLtGhA8p+M1PpX8rBL264lpTBKATbQaAohuyAWRYiJ9/GmtMI+tUvoQfhMfXTCS2jX+9ADcKIZSDwxgnHbDGnZH1NuQCMK99CccUC2tdtyS63gm+NqZu8Y+1v++m9JdvyBO6Nw9LHol/nimvI7kvbZyX+E/gSuXryBnzY4S+f+7O5dZVRar8Olp85k3/uMJA048FrfiMjejIhkod87qFK4b8KoZ/+fcQyEzuM98p+FGVl+/uZQNauI4+mB7TnBM4LxN4f0DB5f4PocpOrUvAucd8nywqPvBN2w/OC2aDpE5jeJO9Q4bFIeM/SeI0Vzg8vjo6xf1ixwunti2mgLieTpsM/wv/bpzBN7x4/pxtU+Pp74FpYnwtJm468ZqxeHhxs/vsBAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class AgreementUpdateRequest:
    """
    Updates details of a billing agreement, by ID. Details include the description, shipping address, start date, and so on.
    """
    def __init__(self, agreement_id):
        self.verb = "PATCH"
        self.path = "/v1/payments/billing-agreements/{agreement_id}?".replace("{agreement_id}", quote(str(agreement_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, patch_request):
        self.body = patch_request
        return self
