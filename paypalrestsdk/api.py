from __future__ import division

import httplib2, base64, json
import logging, datetime, os, platform

import paypalrestsdk.util as util
from paypalrestsdk.exceptions import *
from paypalrestsdk.version    import __version__

class Api:

  # User-Agent for HTTP request
  library_details = "httplib2 %s; python %s"%(httplib2.__version__, platform.python_version())
  user_agent = "PayPalSDK/rest-sdk-python %s (%s)"%(__version__, library_details)

  # Create API object
  # == Example
  #   import paypalrestsdk
  #   api = paypalrestsdk.Api( mode="sandbox",
  #          client_id='CLIENT_ID', client_secret='CLIENT_SECRET', ssl_options={} )
  def __init__(self, options = {}, **args):
    args = util.merge_dict(options, args)

    self.mode           = args.get("mode", "sandbox")
    self.endpoint       = args.get("endpoint", self.default_endpoint())
    self.token_endpoint = args.get("token_endpoint", self.endpoint)
    self.client_id      = args.get("client_id")
    self.client_secret  = args.get("client_secret")
    self.ssl_options    = args.get("ssl_options", {})

    self.token_hash       = None
    self.token_request_at = None
    if args.get("token"):
      self.token_hash     = { "access_token": args.get("token"), "token_type": "Bearer" }

    self.options = args

  # Default endpoint
  def default_endpoint(self):
    if self.mode == "live" :
      return "https://api.paypal.com"
    else:
      return "https://api.sandbox.paypal.com"

  # Find basic auth
  def basic_auth(self):
    credentials = "%s:%s"%(self.client_id, self.client_secret)
    return base64.b64encode(credentials.encode('utf-8')).decode('utf-8').replace("\n", "")

  # Generate token_hash
  def get_token_hash(self):
    self.validate_token_hash()
    if self.token_hash == None :
      self.token_request_at = datetime.datetime.now()
      self.token_hash = self.http_call(util.join_url(self.token_endpoint, "/v1/oauth2/token"), "POST",
        body = "grant_type=client_credentials",
        headers = { "Authorization": ("Basic %s" % self.basic_auth()),
          "Content-Type": "application/x-www-form-urlencoded",
          "Accept": "application/json", "User-Agent": self.user_agent } )
    return self.token_hash

  # Validate expires_in
  def validate_token_hash(self):
    if self.token_request_at and self.token_hash and self.token_hash.get("expires_in") != None :
      delta = datetime.datetime.now() - self.token_request_at
      duration = (delta.microseconds + (delta.seconds + delta.days * 24 * 3600) * 10**6) / 10**6
      if duration > self.token_hash.get("expires_in"):
        self.token_hash = None

  # Get access token
  def get_token(self):
    return self.get_token_hash()["access_token"]

  # Get token type
  def get_token_type(self):
    return self.get_token_hash()["token_type"]

  # Make HTTP call and Format Response
  # == Example
  #   api.request("https://api.sandbox.paypal.com/v1/payments/payment?count=10", "GET", {})
  #   api.request("https://api.sandbox.paypal.com/v1/payments/payment", "POST", "{}", {} )
  def request(self, url, method, body = None, headers = {}):

    http_headers = util.merge_dict(self.headers(), headers)

    if http_headers.get('PayPal-Request-Id'):
      logging.info('PayPal-Request-Id: %s'%(http_headers['PayPal-Request-Id']))

    try:
      return self.http_call(url, method, body= body, headers= http_headers)

    # Format Error message for bad request
    except BadRequest as error:
      return { "error": json.loads(error.content) }

    # Handle Exipre token
    except UnauthorizedAccess as error:
      if(self.token_hash and self.client_id):
        self.token_hash = None
        return self.request(url, method, body, headers)
      else:
        raise error

  # Make http Call
  def http_call(self, url, method, **args):
    logging.info('Request[%s]: %s'%(method, url))
    http = httplib2.Http(**self.ssl_options)
    start_time = datetime.datetime.now()
    response, content = http.request(url, method, **args)
    duration   = datetime.datetime.now() - start_time
    logging.info('Response[%d]: %s, Duration: %s.%ss'%(response.status, response.reason, duration.seconds, duration.microseconds))
    return self.handle_response(response, content.decode('utf-8'))

  # Validate HTTP response
  def handle_response(self, response, content):
    status = response.status
    if status in [ 301, 302, 303, 307 ] :
      raise Redirection(response, content)
    elif status >= 200 and status <= 299 :
      if content :
        return json.loads(content)
      else:
        return {}
    elif status == 400 :
      raise BadRequest(response, content)
    elif status == 401 :
      raise UnauthorizedAccess(response, content)
    elif status == 403 :
      raise ForbiddenAccess(response, content)
    elif status == 404 :
      raise ResourceNotFound(response, content)
    elif status == 405 :
      raise MethodNotAllowed(response, content)
    elif status == 409 :
      raise ResourceConflict(response, content)
    elif status == 410 :
      raise ResourceGone(response, content)
    elif status == 422 :
      raise ResourceInvalid(response, content)
    elif status >= 401 and status <= 499 :
      raise ClientError(response, content)
    elif status >= 500 and status <= 599 :
      raise ServerError(response, content)
    else:
      raise ConnectionError(response, content, "Unknown response code: #{response.code}")

  # Default HTTP headers
  def headers(self):
    return { "Authorization": ("%s %s" %(self.get_token_type(), self.get_token())),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": self.user_agent }

  # Make GET request
  # == Example
  #   api.get("v1/payments/payment?count=1")
  #   api.get("v1/payments/payment/PAY-1234")
  def get(self, action, headers = {}):
    return self.request(util.join_url(self.endpoint, action), 'GET', headers = headers)

  # Make POST request
  # == Example
  #   api.post("v1/payments/payment", { 'indent': 'sale' })
  #   api.post("v1/payments/payment/PAY-1234/execute", { 'payer_id': '1234' })
  def post(self, action, params = {}, headers = {}):
    return self.request(util.join_url(self.endpoint, action), 'POST', body= json.dumps(params), headers = headers )

  # Make DELETE request
  def delete(self, action, headers = {}):
    return self.request(util.join_url(self.endpoint, action), 'DELETE', headers = headers)


global __api__
__api__ = None

# Get default api
def default():
  global __api__
  if __api__ is None :
    try:
      client_id     = os.environ["PAYPAL_CLIENT_ID"]
      client_secret = os.environ["PAYPAL_CLIENT_SECRET"]
    except KeyError as error :
      raise MissingConfig("Required PAYPAL_CLIENT_ID and PAYPAL_CLIENT_SECRET. Refer https://github.com/paypal/rest-api-sdk-python#configuration")

    __api__ = Api( mode= os.environ.get("PAYPAL_MODE", "sandbox"),
      client_id= client_id, client_secret= client_secret)
  return __api__

# Create new default api object with given configuration
def set_config(options = {}, **config):
  global __api__
  __api__ = Api(options, **config)
  return __api__

configure = set_config
