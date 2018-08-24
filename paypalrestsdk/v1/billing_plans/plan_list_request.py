# This class was generated on Mon, 29 Jan 2018 15:08:22 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# plan_list_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/+xcX2/buLJ/v59ioL3A3QCynbb7N29Fkt763jTJadPFWfQUNi2NLG4pUktSSbyL/e4HQ0qyJEup03WNAMcvbTyiqPn748yQ0p/BJcswOAlyweRYcGODMDhDE2meW65kcBJccGMNLLgQXC6Bxpkx3ChIuLCowaboiWBTZoHlOTINXLoLGk2upMEQTI4RT1agJILSkCmNoNwjmIDfC9QrYDKGnC25ZESGnGmWoUVtxkEY/IOGXNek4OTDn8HNKifWjdVcLoMw+IVpzhYCK5HYEoMw+H9clYQN0W5ShD9QqxGXMd5jDLLIFqhBJY77hGtjiSX0si1wyZ2cCAYtjaJrleCaxLWFlhh3xR/DGSasEBa4gfnxnAR6qTVbeQmOw+AtsvhKilVwkjBhkAi/F1xjXBOutcpRW44mOJGFEH+FWylgZvgfW2hhLXhpSwXkDKAkMDBcLgU6YcfwSmnAe5blAkPgCczrp8yddM+O5yEgi1KvOJOqOwMWZeU5L+GWCR7TvwXSHQykkiOJS2b5LYbuFxkFuLS4RN1W3rO9ac9YZgvzsOpeuRgwjSDoWB4WK2DuEvj59sS8VZaJma5melCIqYx5xCwauEvRpmVM1xJwGYkiRi/k3E/MLWZm7iK2pLhImEPCUcRmDL9U1p2viKw0zKXajeU+hsFrZDHqFhp8DINXSmdd2jWzaZdGj0BjPQ80JZG8sJ5Wa/ea7HbhQbGj4IdV+rKMnqTy+lMlLSPwiNEyLgwkFEYuSugZpEhWgcqH1y9vzq9evgPB5Sfz8dtJrCIzYTmfqFvUtxzvJt+kzKJiZuSGHP1dva6x9ILLT9CQBa4Wv2HUI797cEsJFaWjCQmMOCPBtFf8SKNgFuO/L+gPXy7oUOCkGpOWWCVhEzIjRRhoESzTS7Tw/u2FWxcz9gnLCPJiRkyIkIYvuPRXMrSpiuGO2xRsyo1TQEjY8eH92ylYzHK6lZwkY/bjt6m1uTmZTKxSwow52mSs9HKS2kxMdBL98P2Px0djmPpA9XH63/MQ5t/OQx+jR3OIUqZZ5NCKfC/XOMq1itAQuo+BJJqTrA7FaYpPuILKQCSrkiitX+ucMYDVKvAyenkYmGJhyNLSOvKeEM/rtGW6mrRpvNc3N9eVGSqUpEWv13h7kkCjaLHvf2/y/oHU7xmkCLWrHD/rIt///NNP3xiM6I7Rd0ch3KU8SsGgvkUDzACTMD1znsGceb2hC8myBV8WqjBiBbFjZYFVCpQxaXlkqnSJbhvDO0T44GDkbcmhWXN3d3c35kwyxxszhi9lhtKaCd07qkTq/hzfkxhHu1k9GoYgeO/JmgixW4aoKMPI5lH+q4NTpJFZnFmetVO6Nn3TY2ICEwICGkGrvKwzFrhjBvz9sUegqbSoJdrOXVti0YsXL36uHe378Q9HewqeuCF0UzVt+qZqnA4ag8bwht3zrMhAoFzalNDw2fMfyxx4tFiRTkSeMllkqHnUwNU9ScrbIMf7AW56VoWlq+x2y9ohSzhkCYcs4ZAl/EdkCW9QRymTFq41JqhRRmj6HMuPmuWtUU036x2wabhqIDQGlip3UF5FsIFU3UFWRClwC5Ey1rVtqIgscqdqttSIpLnQ/Xz/9sKV+Nr7blQYqzLUEFEBmuda3brWXMRkhKJvgqxcGdfNIiaEusMYEsYFxpCzFY0GZgmcrAnrjsI1W10zAaywKmOWU7ysXE/Re4kqrLFMxlwuYcEEcVB1UiTe27r7GK0igR6tHH/OU4EnLYH+xwCX3HImaoaIP7O7KnkoNlkUYW4xnpXPnVHUtbxgaERPYlKyTgMaLcZqAucRblXwTkGijJQUvo2q0cWsH5UUttAIhcE9QRRZeUYmm7FMFdK2NbB58XPtqF06j1/Dem/xs7l2FnjenIvLFUXiLffoVnq6iVKMi4bPN3peJ/8qjo9fRIVw/6P/JXjzV6Ri/xdeXnnKZE0aVwLHCg1IZXskb0fwgBZandNtHlxS2rwOcf7r+bth1ods9VmWe1moVLkf9/UAOCt0e6FtkTfj9f3biyFw7UPUR4Wi1cUXipIyPTPYjsAGsSdfrRJAt5A8YZApIX5GAVlCycyvB+3y6KFhm+I/ckX5spg/vbq8mV6+P+8Jn5umj4DGzDWNiatbrJe97mrrsYobYHHsE9RBQJgmLjRHFSZyAyhJq3G4Y5htbtpUAs8fhzCnLy9Pzy82tFQx6rsWph1XsCgsua4Bbo3bcyFIhxw944W03Edi16CRQKaN09DwZZ8HVZM1HoqRyrAy1OAkzmmG5uCmBAqM+9U0aXvXQqjo0++FstikGquVXJYQryyWjjlp0uFXVThgKkxZBxq0RT5LEOflvhwzLQFKFyPP0ny5LPF7PhxctaW7XO6pzGP3JVNlJtpOxXuu9uThj812u7u8VfnkbiMESUhfOHj7flQjleXJamN1a5G3Xt24y094wgl2KEVtx2Kjt/i0Fg+/Ub+hhBb5UUt8VT99xTX+tNBUDK56dqqr6G0J06RuyrJgBkG5tp0vLoWAhEsmI4p3BwJ1B85v6oZgqNZkpkL/sHbhuCiLMqNAya9fZ0VrVTTSmjWxpxtiU404Wmc303dXo++eP/sRqtuAFph1DyLGWxTE0zhnq5yJcaQy33l0xxK06zlMYq4xshONxk6qiUY0kZkc7SfDc5Zq6aGi9OR2lahuyBje8GVKaxcwWR22cL5QjuNoQPBPCP93/eu6AKV6xK7yMj1ItMd7JsB1KGKMeMZETe+d7+bybD2fKRYxv+WxOzXjUhdVGCZjmxp/2MT32crm2xqMqyflgq0bJC1jhmAQ4cP03RWQpTv9JaNce4kbNUlVhhOX2zAdm9qQM2fIcWqzndjyY6urNAjPrLO3UxIGdi7o6o4x87oM6jN065XPlDdOFvnuRVyP6eyY9V7vnpGo4aMeVS2ZMVrUGZdlk0slFv0hCTIzUYSSy42liKJ7SUvNtHlkhTxb31ISY8vZB+7ziZn/UWY8HtXqc2om5XlOWVuClOxROs7ucYcbf8MY39dJ6e+fHND9gO4HdN8/ujcyNQ8hb1Ts9mZ6ejJLnGV01Ww0ZppXhvdID0B0AKIDEB2A6DNAtKsjJGVO5IBpXweYuztngxtlTebcblmVRHJDqEgOU8HlzveGB5FjFYnO/m9NevDwfdVtdIO9Y9Z9I3/AvDw+oXFZCKZ7c2iDFuZ+ijlYtcc3DhJ3eKcLmU3qpvT11frAUimSay5z0xBt31LMqtqhX5zm5U25tq47ql2EiElCvQXC0vXMCJOYhGfPIVOScOqJni/b8MB9dTK3L5U3WPwahfPfh7IePmnsGM7rNwWywlhI2S2SWwlk7h0dfAAOKGEK6xJWrEJgYHVzV6JhOP+gxs3+tS3+ZXX4vtDW7fK0e58lZaBr8lVexblBnfUcDLIluWH+kjKc3rsRu9h8/YoVwEwz2Xm/rnPhUA0cqoFDNfD0q4FFsUI9w5hbIrbMunFpmzcHWxtjdK/fFStPKZRJHUHcE01oHPrumLdhNM3Y/aw8OtF3XK738gFZD8h6QNanj6wqKh/e6QW06Q81BCzPqtO/mZK4cpi6QMgLITCGuKAH7x1Rt69oiClfw+yrGHhEtUWlgK+v+heyzQKpfr/f3evLMEh4+9MRrZ5Np6HzRecFX03/eX42cFiwZMT08NF59qOO3k0vX00vpzfnn3tqJWhIUncnOd64O9yKqcl+z/sWedz7VmWb/vi3Kv39T/ityo9bf0jCfe+hHVUtek/gu2P03c+KlNEjuLF7/RCG+zpFD/8VfQv+3ZdeNr7r4l6Ia3wBpXx5sTxF2TnGkLl3CZwiys/kKLn+VEo52eYHNoamN27BLYw/8hsxERXufUC7Nfs7cqLgVEmLsvyiRsDyXBCaUkb1m3HHR15bm7/x79mdBP97fhP4L3MEJ8Hk9tmkeoViUia6I6ejSRAG5/c5Rhbjd65hc6piDE6eHx//9V//BgAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class PlanListRequest:
    """
    Lists billing plans. To filter the plans that appear in the response, specify one or more optional query and pagination parameters.
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/payments/billing-plans/?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def page(self, page):
        params = str(page)
        self.path += "page=" + quote(params) + "&"
        return self

    def page_size(self, page_size):
        params = str(page_size)
        self.path += "page_size=" + quote(params) + "&"
        return self

    def status(self, status):
        params = str(status)
        self.path += "status=" + quote(params) + "&"
        return self

    def total_required(self, total_required):
        params = str(total_required)
        self.path += "total_required=" + quote(params) + "&"
        return self

    
