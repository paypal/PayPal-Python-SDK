import base64

from braintreehttp import Environment


class PayPalEnvironment(Environment):

    LIVE_API_URL = 'https://api.paypal.com'
    LIVE_WEB_URL = 'https://www.paypal.com'
    SANDBOX_API_URL = 'https://api.sandbox.paypal.com'
    SANDBOX_WEB_URL = 'https://www.sandbox.paypal.com'

    def __init__(self, client_id, client_secret, apiUrl, webUrl):
        super(PayPalEnvironment, self).__init__(apiUrl)
        self.client_id = client_id
        self.client_secret = client_secret
        self.web_url = webUrl

    def authorization_string(self):
        return "Basic {0}".format(base64.b64encode((self.client_id + ":" + self.client_secret).encode()).decode())


class SandboxEnvironment(PayPalEnvironment):

    def __init__(self, client_id, client_secret):
        super(SandboxEnvironment, self).__init__(client_id,
                client_secret, 
                PayPalEnvironment.SANDBOX_API_URL,
                PayPalEnvironment.SANDBOX_WEB_URL)


class LiveEnvironment(PayPalEnvironment):

    def __init__(self, client_id, client_secret):
        super(LiveEnvironment, self).__init__(client_id, 
                client_secret, 
                PayPalEnvironment.LIVE_API_URL,
                PayPalEnvironment.LIVE_WEB_URL)
