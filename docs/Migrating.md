# Migrating from Version 1 to Version 2

## 1. Initialize SDK

#### BEFORE
```py
paypalrestsdk.configure(client_id, client_secret)
```

#### AFTER
```py
import paypalrestsdk.core as paypal

env = paypal.environment.SandboxEnvironment(client_id, client_secret)

client = paypal.paypal_http_client.PayPalHttpClient(environment=env)
```

# 2. Make a call

#### BEFORE
```py
from paypalrestsdk import Payment

payment = Payment({
    "payer": {
        "payment_method": "paypal"
    },
    "intent": "sale",
    ...
  })

if payment.create():
    print("Payment[%s] created successfully" % (payment.id))
else:
    print("Error while creating payment:")
    print(payment.error)
```

#### AFTER
```py
import paypalrestsdk.v1.payments as payments

payment_create_request = payments.PaymentCreateRequest()
payment_create_request.request_body({
    "payer": {
        "payment_method": "paypal"
    },
    "intent": "sale",
    ...
})

try:
    payment_create_response = client.execute(payment_create_request)
    payment = payment_create_response.result
    print("Payment[%s] created successfully" % (payment.id))
except IOError as ioe:
    print("Error while creating payment:")
    print(ioe)
```

