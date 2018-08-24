from braintreehttp.serializers import FormEncoded

class UserConsent(object):

    def __init__(self, paypalenvironment):
        self.url = '{}/signin/authorize?client_id={}&'.format(paypalenvironment.web_url, paypalenvironment.client_id) 
        self.params = {}

    def response_type(self, response_type):
        self.params['response_type'] = response_type
        return self

    def scope(self, scope):
        self.params['scope'] = scope
        return self

    def redirect_uri(self, redirect_uri):
        self.params['redirect_uri'] = redirect_uri
        return self

    def nonce(self, nonce):
        self.params['nonce'] = nonce
        return self

    def state(self, state):
        self.params['state'] = state
        return self

    def build(self):
        for key, value in self.params.iteritems():
            self.url += key + '=' + value + '&'

        return self.url
