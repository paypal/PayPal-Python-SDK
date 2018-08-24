class RefreshTokenRequest:

    def __init__(self, paypal_environment, authorization_code):
        self.path = "/v1/identity/openidconnect/tokenservice"
        self.verb = "POST"
        self.body = {
                'grant_type': 'authorization_code',
                'code': authorization_code
                }
        self.headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": paypal_environment.authorization_string()
                }
