import paypalrestsdk
from paypalrestsdk.openid_connect import Tokeninfo

paypalrestsdk.configure({
    'client_id': 'CLIENT_ID',
    'client_secret': 'CLIENT_SECRET',
    'openid_client_id': 'CLIENT_ID',
    'openid_client_secret': 'CLIENT_SECRET',
    'openid_redirect_uri': 'http://example.com'
})

login_url = Tokeninfo.authorize_url({'scope': 'openid profile'})

print(login_url)

code = raw_input('Authorize code: ')

tokeninfo = Tokeninfo.create(code)

print(tokeninfo)

userinfo = tokeninfo.userinfo()

print(userinfo)

tokeninfo = tokeninfo.refresh()

print(tokeninfo)

logout_url = tokeninfo.logout_url()

print(logout_url)
