# PayPal REST SDK [![Build Status](https://travis-ci.org/paypal/rest-api-sdk-python.png?branch=master)](https://travis-ci.org/paypal/rest-api-sdk-python)

The PayPal REST SDK provides Python APIs to create, process and manage payment.

## Installation

Install using `easy_install`:

```sh
easy_install paypalrestsdk
```

Install using `pip`:

```sh
pip install paypalrestsdk
```

## Configuration

```python
import paypalrestsdk
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM",
  "client_secret": "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM" })
```

Configure through environment variables:

```sh
export PAYPAL_MODE=sandbox   # sandbox or live
export PAYPAL_CLIENT_ID=EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM
export PAYPAL_CLIENT_SECRET=EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM
```

### Create Payment

```python
import paypalrestsdk
import logging

logging.basicConfig(level=logging.INFO)

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM",
  "client_secret": "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM" })

payment = paypalrestsdk.Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "credit_card",
    "funding_instruments": [{
      "credit_card": {
        "type": "visa",
        "number": "4417119669820331",
        "expire_month": "11",
        "expire_year": "2018",
        "cvv2": "874",
        "first_name": "Joe",
        "last_name": "Shopper" }}]},
  "transactions": [{
    "item_list": {
      "items": [{
        "name": "item",
        "sku": "item",
        "price": "1.00",
        "currency": "USD",
        "quantity": 1 }]},
    "amount": {
      "total": "1.00",
      "currency": "USD" },
    "description": "This is the payment transaction description." }]})

if payment.create():
  print("Payment created successfully")
else:
  print(payment.error)
```

### Get Payment details

```python
# Fetch Payment
payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")

# Get List of Payments
payment_history = paypalrestsdk.Payment.all({"count": 10})
payment_history.payments
```

## Execute Payment

Only for [Payment](https://github.com/paypal/rest-api-sdk-python/blob/master/samples/payment/create_with_paypal.py) with `payment_method` as `"paypal"`

```python
payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")

if payment.execute({"payer_id": "DUFRQ8GWYMJXC"}):
  print("Payment execute successfully")
else:
  print(payment.error) # Error Hash
```

For more samples [github.com/paypal/rest-api-sdk-python/tree/master/samples](https://github.com/paypal/rest-api-sdk-python/tree/master/samples)


## OpenID Connect

```python
import paypalrestsdk
from paypalrestsdk.openid_connect import Tokeninfo, Userinfo

paypalrestsdk.configure({
  "openid_client_id": "LIVE_CLIENT_ID",
  "openid_client_secret": "LIVE_CLIENT_SECRET",
  "openid_redirect_uri": "http://example.com" })

# Generate login url
login_url = Tokeninfo.authorize_url({ "scope": "openid profile"})

# Create tokeninfo with Authorize code
tokeninfo = Tokeninfo.create("Replace with Authorize code")

# Refresh tokeninfo
tokeninfo = tokeninfo.refresh()

# Create tokeninfo with refresh_token
tokeninfo = Tokeninfo.create_with_refresh_token("Replace with refresh_token")

# Get userinfo
userinfo  = tokeninfo.userinfo()

# Get userinfo with access_token
userinfo  = Userinfo.get("Replace with access_token")

# Generate logout url
logout_url = tokeninfo.logout_url()
```
