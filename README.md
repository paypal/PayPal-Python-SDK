# PayPal REST SDK 

Continuous integration status:

[![Build Status](https://travis-ci.org/paypal/PayPal-Python-SDK.svg?branch=master)](https://travis-ci.org/paypal/PayPal-Python-SDK) [![Coverage Status](https://coveralls.io/repos/paypal/PayPal-Python-SDK/badge.svg?branch=master)](https://coveralls.io/r/paypal/PayPal-Python-SDK?branch=master) [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/paypal/PayPal-Python-SDK)

The PayPal REST SDK provides Python APIs to create, process and manage payment. The [Paypal REST APIs](https://developer.paypal.com/webapps/developer/docs/api/) are fully supported by the sdk.

> The REST APIs are getting closer to parity with older merchant APIs. Check out https://github.com/paypal/PayPal-Python-SDK#explore-further-payment-capabilities

> If deploying on Google appengine and running into issues since requests is a dependency, see [#66](https://github.com/paypal/PayPal-Python-SDK/issues/66) for workaround.

> **The Payment Card Industry (PCI) Council has [mandated](http://blog.pcisecuritystandards.org/migrating-from-ssl-and-early-tls) that early versions of TLS be retired from service.  All organizations that handle credit card information are required to comply with this standard. As part of this obligation, PayPal is updating its services to require TLS 1.2 for all HTTPS connections. At this time, PayPal will also require HTTP/1.1 for all connections. See the [PayPal TLS Update repository](https://github.com/paypal/tls-update) for more information.**

> **TLSv1_2 warning: Due to PCI compliance, merchant servers using a version of TLS that does not support TLSv1_2 will receive a warning.

> **To verify that your server supports PCI compliant version of TLS, run [this sample](/samples/payment/create_with_paypal_security_test.py) with your sandbox client_id and client_secret.

## System Requirements
PayPal SDK depends on the following system libraries:

* libssl-dev
* libffi-dev

On Debian-based systems, run:

```sh
apt-get install libssl-dev libffi-dev
```


## Installation

Install using `pip`:

```sh
pip install paypalrestsdk
```

## Configuration

 Register for a developer account and get your client_id and secret at [PayPal Developer Portal](https://developer.paypal.com).

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

Configure through a non-global API object
```python
import paypalrestsdk
my_api = paypalrestsdk.Api({
  'mode': 'sandbox',
  'client_id': '...',
  'client_secret': '...'})

payment = paypalrestsdk.Payment({...}, api=my_api)

```

### Create Payment

```python
import paypalrestsdk
import logging

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

### Execute Payment

Only for [Payment](https://github.com/paypal/PayPal-Python-SDK/blob/master/samples/payment/create_with_paypal.py) with `payment_method` as `"paypal"`

```python
payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")

if payment.execute({"payer_id": "DUFRQ8GWYMJXC"}):
  print("Payment execute successfully")
else:
  print(payment.error) # Error Hash
```

### Subscription

Create [subscription payments](https://developer.paypal.com/docs/integration/direct/create-billing-plan/) i.e. planned sets of future recurring payments at periodic intervals. Billing plans serve as the template for a subscription while billing agreements can be used to have customers subscribe to the plan.

#### Create a billing plan

```python
from paypalrestsdk import BillingPlan

billing_plan = BillingPlan({
    "name": "Fast Speed Plan",
    "description": "Create Plan for Regular",
    "merchant_preferences": {
        "auto_bill_amount": "yes",
        "cancel_url": "http://www.paypal.com/cancel",
        "initial_fail_amount_action": "continue",
        "max_fail_attempts": "1",
        "return_url": "http://www.paypal.com/execute",
        "setup_fee": {
            "currency": "USD",
            "value": "25"
        }
    },
    "payment_definitions": [
        {
            "amount": {
                "currency": "USD",
                "value": "100"
            },
            "charge_models": [
                {
                    "amount": {
                        "currency": "USD",
                        "value": "10.60"
                    },
                    "type": "SHIPPING"
                },
                {
                    "amount": {
                        "currency": "USD",
                        "value": "20"
                    },
                    "type": "TAX"
                }
            ],
            "cycles": "0",
            "frequency": "MONTH",
            "frequency_interval": "1",
            "name": "Regular 1",
            "type": "REGULAR"
        }
    ],
    "type": "INFINITE"
})

response = billing_plan.create()
print(response)
```

Check out [more samples](/samples/subscription/). The [Subscription REST APIs](https://developer.paypal.com/webapps/developer/docs/api/#subscriptions) are fully supported by the sdk.

Also, check out a [flask application](/samples/subscription/ppsubscribe) demonstrating the use of subscription APIs from both merchant and customer points of view.

### Future Payments

Check out this [sample](/samples/payment/create_future_payment.py) for executing [future payments](https://developer.paypal.com/docs/integration/mobile/make-future-payment/) for a customer who has granted consent on a mobile device.

### Third Party Invoicing

Check out this [sample](/samples/invoice/third_party_invoicing.py) for executing third party invoicing for a merchant who has granted consent to send invoice on their behalf.

### Orders

Create and manage [Orders](https://developer.paypal.com/webapps/developer/docs/integration/direct/create-process-order/#create-the-order), i.e. getting consent from buyer for a purchase but only placing the funds on hold when the merchant is ready to fulfill the [order](https://developer.paypal.com/webapps/developer/docs/api/#orders), have a look at [samples](/samples/order)

### Payouts

For creating [batch and single payouts](https://developer.paypal.com/webapps/developer/docs/integration/direct/payouts-overview/), check out the samples for [payouts](/samples/payout) and [payout items](/samples/payout_item). The [Payouts feature](https://developer.paypal.com/webapps/developer/docs/api/#payouts) enables you to make PayPal payments to multiple PayPal accounts in a single API call.

#### Create a synchronous payout

```python
from paypalrestsdk import Payout, ResourceNotFound

payout = Payout({
    "sender_batch_header": {
        "sender_batch_id": "batch_1",
        "email_subject": "You have a payment"
    },
    "items": [
        {
            "recipient_type": "EMAIL",
            "amount": {
                "value": 0.99,
                "currency": "USD"
            },
            "receiver": "shirt-supplier-one@mail.com",
            "note": "Thank you.",
            "sender_item_id": "item_1"
        }
    ]
})

if payout.create(sync_mode=True):
    print("payout[%s] created successfully" %
          (payout.batch_header.payout_batch_id))
else:
    print(payout.error)
```

### Explore further payment capabilities

For [exploring additional payment capabilites](https://developer.paypal.com/docs/integration/direct/explore-payment-capabilities/), such as handling discounts, insurance, soft_descriptor and invoice_number, have a look at this [example](/samples/payment/create_with_paypal_further_capabilities.py). These bring REST payment functionality closer to parity with older Merchant APIs.

### Customizing a PayPal payment experience

Customizing a [PayPal payment experience](https://developer.paypal.com/docs/integration/direct/rest-payment-experience/) is available as of version 1.5.0 enabling merchants to provide a customized experience to consumers from the merchant’s website to the PayPal payment. Get started with the [supported rest methods](https://developer.paypal.com/docs/api/payment-experience/) and [samples](/samples/payment_experience/web_profile).

### Webhooks - Receive notifications about PayPal Payments

To receive [notifications from PayPal about Payment events](https://developer.paypal.com/webapps/developer/docs/api/#notifications) on your server, webhook support is now available as of version 1.6.0. 

- For creating and managing [Webhook and Webhook Events](https://developer.paypal.com/webapps/developer/docs/integration/direct/rest-webhooks-overview/), check out the [samples](/samples/notification/) to see how you can use the Python sdk to create and manage webhooks and webhook events.
- See this [sample](/samples/notification/webhook-events/verify_webhook_events.py) for verifying that the webhook response is unaltered, from PayPal and targeted towards the intended recipient.
- See this [sample](/samples/notification/webhook-events/get_webhook_event_resource.py) for parsing webhook payload and getting the resource delivered via the webhook event.

### Invoicing

Create, send and manage [invoices](https://developer.paypal.com/docs/integration/direct/invoicing/).

#### Create an invoice

```python
from paypalrestsdk import Invoice

invoice = Invoice({
  'merchant_info': {
    "email": "default@merchant.com",
  },
  "billing_info": [{
    "email": "example@example.com"
  }],
  "items": [{
      "name": "Widgets",
      "quantity": 20,
      "unit_price": {
        "currency": "USD",
        "value": 2
      }
    }],
})

response = invoice.create()
print(response)
```

### OpenID Connect

```python
import paypalrestsdk
from paypalrestsdk.openid_connect import Tokeninfo, Userinfo

paypalrestsdk.configure({
  "mode": "sandbox",
  "client_id": "CLIENT_ID",
  "client_secret": "CLIENT_SECRET",
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
### Debugging
* Include Headers and Content by setting logging level to DEBUG, particularly for
  Paypal-Debug-Id if requesting PayPal Merchant Technical Services for support
  logging.basicConfig(level=logging.INFO).
* Full request and response headers and body is visible at DEBUG level logging only
  for sandbox or non-production mode. This is done to prevent sensitive information
  from getting logged in live mode.

Check out [more samples](/samples/invoice/). The [Invoicing REST APIs](https://developer.paypal.com/webapps/developer/docs/api/#invoicing) are fully supported by the sdk.

## License
Code released under [SDK LICENSE](LICENSE)  

## Contributions 
 Pull requests and new issues are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for details. 
