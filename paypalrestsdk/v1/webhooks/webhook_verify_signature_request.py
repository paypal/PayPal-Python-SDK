# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# webhook_verify_signature_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/9RY0XLbthJ9v1+xw3sf4hmJ8m3qNNGbxnZiTZ1YteS0HY/HWpErETEJsMBSMpvJv3dAkLJIWpHTOG76pNHugtxzdrE4xEfvHSbk9b0VzSKlbvwlaTHPr41YSORMk9fxjsgEWqQslPT63nsbIMgAQrkG1sG+1/F+yUjnI9SYEJM2Xv/yquOdEIakm9bXSidN2wg5atrO6Y+MDE/ylLz+R8/9ukRy+LVMYryR8XvUAmcxldgcpm6ZbncT28+U7w6qEzAAF9qGD9olamkYaI25y3TfIsDwTMa5159jbMhBEprCtWGkVUqaBVnMa4yGtZCLNiLMOLrGeKFqEDat9ZwnEYF1aMFRAhwhwwjzEcaQGTLAChYkSSMTcEQbiFCGLjxXGQQobbwNLymoBftwfMsaAwaOhIElxhnBXKukCJuOBr+PBqfdwcXkpDs4fXM2BU0mVdIQREV7dGAViSACYUBTQGJJIawER8XyimypWMxFgBbYF/HMOmvQLLM4/tTZyXVAmq8zHdeo3jC2mf7NP9h/BWk2i0UAN5SDjXZZkw9HaiVjhWEBa8NTUSUMXJyfFsxbsgV/Hd+Hx+eT7sX56b+FbtYoTSKMEUpei7DGetvXJn94BGpeYDiZTEawucSHQyUZhaQQhKyxNDkfvBu/HY7Hw7N33eHRtOSoetQmDZCQMbigf4AOIxbb+XDONiFuo3erDR4CmjxJiLUINntpkKaE2nyWmPHwzXfKDIuEtlNTetvchHbfFTNOJLS1bzqWlMuhZNKSuLFornSCfPUsYk5Nv9djpWLjC+K5r/SiF3ES9/Q8eP78+av/Ggrsy7sH/ou9hzE+Gb49fnrKj5ckuc14ORSuqXTfsd30NE/MapwU/sccKruPykATMrUbpG7f1RqriGRtMLaRwAoNuKeG36ZjvlJWPHBfFciu2QZt8lUzt+lyfBRSgbVYLEhTuIOwJ8WzJG238j2Q7jzbUJUR1Ub96rPx72NpnIc7j8AnI/9UyBvYyATOZh8ouGeGxELemBqIytKYGRLQpmeRlLK6qykuDrDLk8Hk+GwwhmLp1bNeqALTw1T0ImRSaLqFo7lhXjy+Do80zWtgSkO7JoFK0pisvka9ILYSz4eJggRvnOauwAUYxx0bPhPSeRLiSK21mTAFbDdhLs6HwJSkcaEfHzZXXhz8tL/nw1AGcRa6N0z/N+3A9Nm0Uwyp6d4UggitsiRt7GMh1dRNtQrIGCEXPlhEU4t1auWjfYSVuVVZLFYl1/OgKAbgmgKH0eFBMNnM2PpKLsxPtJEcp7XSrU3t4hWKoCyDLt9uVfm9xXsiBJrqXyTufzv3S0u/S9DuSzvAd7bIwauXL9dHz4971ZeCIb20H/4GUNohYzsDi/K6QmcSk5lYZCozcQ5hkcqMXH8YSlCyCEw1muwyH8ZEcFkMj/MyQ3OX3Wq18gVKLHJDY8VqQpJNz67tVpCaf/1bC+NxTsurjUKoLRNNk1GZDqhRjbWxXZLK+V0el1VybQXQ9LSBSbxT0WuQ1d5gtfX0dGifCKDJkgR1XoN2Z2sq19JTdrM722zf81od1GoEr5UGukU76TowHUCKue1ZwIwjpcWfLanoTx+7UbcBr0R6Q0TUzA8REzZ3JedikWn3IZ2rTMMRLSm2WcFIacYYMAhU9oVV3fJlcvXJBrnbiwfeAkIV3+ahhv5ezJ+54HMP/fY3fEUKZVddG0bOTPu6suVvQ3GuqoR3SDbXP1aJDpVkkuU9rYdpGpcv6H0whcA+YU7fumO2743OxhPPXfh6fa+3/H9vcyeZ3mcuZI9vUwqYwnEB7lCF5PV/2N//9J+/AAAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhookVerifySignatureRequest:
    """
    Verifies a webhook signature.
    """
    def __init__(self):
        self.verb = "POST"
        self.path = "/v1/notifications/verify-webhook-signature?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, verify_webhook_signature):
        self.body = verify_webhook_signature
        return self
