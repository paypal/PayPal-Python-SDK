# This class was generated on Mon, 29 Jan 2018 15:08:24 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# web_profile_list_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/8xZX3PbuBF/76fY4cu1M7LkpNPrVDN9cPy/yTmqrVwe2gy1IlckEhDgAaBl+ua+e2cBUhIp6WwnjnsPhiXsAtjf7m8Xf/RrdIUFReNoSfOD0uiFkDSUwrpoEJ2QTYwondAqGkfvhHUWUEpY0hzoriQjSCUEzSgLC20AoSCT5KgcaAO2mn+mxA2jQfTvikw9QYMFOTI2Gv/n0yC6IEzJ9HvPtCn6fRN0eb/vmn6pyLppXVI0VpWU3GVLrSyFvl+j8D/6SHOYBDOjQfQzGoFzSQ3yaBC9pXr9pQv7SAEagzXohQfeomVMRywIS/zIa2P6Xsk6Gi9QWgr2CUPpqmNidEnGCWIAK+POpF7CsVYLkW0bt5B6GSetcG1nt79r8jQnYDkEeWWQBVCu3Nez/fDrbbfOCLXD7DmqL7G7U3FJKhUqiysjO/bvUdgGsqKTFY7gw/U7cBpSYUuJNeDCEXOOZwNnUNkFGSixLki5IVwqOCdToKoHcItSpKCVrD1PXU5wLowusW71oSCX65R5u3O+Rv6tzmOi/jZ40IMSg19KzCh2rLvpvl3Sbd+xgHnbaANrb7pPK++HCdYTlMHB7JvKkoEkp+SLrtwQppp7vKbS6qDRxiTRlXKduQdgyfECszdCSqGyWWd0f6TOhNoz/h3LZi/kakOuMiqujIhz58o4xLnj770q206/mE4nLZVcA16DoVQYSpx3RFJZpwsyLEAIczO1h/AzyopAWJidn05nTMXZ5P3N9KU8wZGPMfFoNuF3+7uYJ4YsKWeBhMspZNZ/q8PDvybWGa0y/5mOtXJCVRQko00Ro9weMMEarvRyl35LzVDknO74dBhGzM0oaPe+ntACK+nYxU8ycrC2MtFp0KANt/wz6Y5dKw3hY04Kal1BqkFpB18Um81FWiiUq/KCBafFgPODSiaKsJA25jLSASxzkeQrKtktLm0kWTupT/mlcPlXxGVeOadVY39nrUSK5MuTPdidAhVwYc9Cbeg64YEgrj36gCu5nPx+0IpCuK2QsS+TXOumbj2JnN8tUr+z5lcEav9sg048hOUTT0LWUgqiKCgV6EjWz1KQPj2iJIluIRa7i+7lCe9zbPjuw+kz189LVVYOzgTJ1O4wmaXxopVuGN8VbMPwCuAVmhiK++93eBPKUUZmGwCmqSFrY31Lxoi0e/TYIewCuVSpSNCRhWVOYUtYHzk4RDYXZcl7fjMVuBwD09DTzOeHsJDwZcNgs6tgoLZW/Acc1OYgJyzMq5pM7zizSQLMyK4313FgfSU3i4sUm9/WteBwR0E/CWDsbjSNdU0NG3Un3rfMqycvY0tKxEJwWqq1v4ZbVZZ3HEpFs6H0p9lt5aj1zfOmzVxrSah2EE7ydUZp16PaZveDJOvvLqTC5YDHtzV3fTlV3RqcEaQVV6D1wfd5se9NNqXjNigd8N3+h9A3QNKWMlt0CVWnxf3/TI6e3+23J8o1pci77D7QC6OL7WXhTBtIRSYcSsi0Tu0g5Eiov8KCaeILqFIoKutgTvAIg54E6PUOQOfk9vhvBaWl+g92daFq97rvn9KP2bgV/+sQOnRs73q7t2xg/SH81Li9UuKXipo3Jj7X6cW+l6dnztzmgoPN7acHs+xK13B7gm3Y1tWSPLU2VV/2mcagSuOtSHW6e89hIHFOMmzZ7REgcHVeWaGYozwwbEpbd/5d6Q/HORpMuFhLUpnLvU+kKETwiB3Dq9d/BytUJulgXjsClGWOqirIiIRvEWG4famnGZ2gpJgTtvso0+nfDniQe+Iy8ODDHTeBjVxo6/kQjpoXrNvVC8HRh9kAZkdTbt+c+vaa2+Mj31749orbEy89veH2/A23Z17z0o+9esftJLS+55pn1gZmH25mvPLfDlY+BkbHy6O0ujGJs0+iyiqPKgTeEviIG0F2DLMU45O3PHVO8aVfSaTx5Ql/+Izxvyb8Qen46j1/KF0ckJgq9qbM7G184zG4PJ56YPd5HLDd5/HF28bc+zyefpy9GAsyHYsCsz4JNrr7udM8XzpPhkyD11vH1t+uwqsdB3iYiQVDHH4uswbhsAyPanxX4LE/WCjwThRVAUuRupzHvfrHIZTijqQN+1Yjz0lkuT9m/9jKhy3zEqNLG2ZsaImGQKLJyKyUSokJWb52mw3roeGw02V7BUvQODB0K2jJ8+BqBkN84SaVNovwDd46bcI1O0ynla/vSWUI/nwxnU5u/gKWzC0b8p6POkthaeD3jLnRS0vGrp+DoSBr/SMnT796JwrplmjlUCj/iNksIBwVf7gC9OkxJ2ZHRakNmrpDvs3ex5yX2622JGP9zzvhRmWIINeVscy50r+gk3Ky9q+5jW5/fKuzfsP1+GZ7x/SWWo9zpqLZc3kyOtbKkWp+JIqwLCX7QWg1+mz9xnzhXPlTeM4dR+en0yj82BSNo9Htq1FTkw/WNXm08UuZHUWD6PSupMRReuPQVfaYq//49eHhb3/6HwAAAP//
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebProfileListRequest:
    """
    Lists all web experience profiles for a merchant or subject.
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/payment-experience/web-profiles/?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
