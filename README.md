# PayPal SDK 2.0.0-beta

This is a preview of how PayPal SDKs will look in the next major version. We've simplified the interface to only provide
simple model objects and blueprints for HTTP calls. This repo currently only contains functionality for working with payments and invoices
to serve as an example and early beta of the API going forward.

## What's New

Please see the [CHANGELOG.md](./CHANGELOG.md) for the latest changes.

### Creating a Payment

```python
import paypalrestsdk.core as paypal
import paypalrestsdk.v1.payments as payments
import braintreehttp

client_id = "AYSq3RDGsmBLJE-otTkBtM-jBRd1TCQwFf9RGfwddNXWz0uFU9ztymylOhRS"
client_secret = "EGnHDxD_qRPdaLdZz8iCr8N7_MzF-YHPTkjs6NKYQvQSBngp4PTTVWkPZRbL"
env = paypal.environment.SandboxEnvironment(client_id, client_secret)

client = paypal.paypal_http_client.PayPalHttpClient(environment=env)

payment_create_request = payments.PaymentCreateRequest()
payment_create_request.request_body({
    "payer": {
        "payment_method": "paypal"
    },
    "intent": "sale",
    "transactions": [{
        "amount": {
            "total": "10",
            "currency": "USD"
        }
    }],
    "redirect_urls": {
        "cancel_url": "https://example.com/cancel",
        "return_url": "https://example.com/return"
    }
})

try:
    payment_create_response = client.execute(payment_create_request)
    payment = payment_create_response.result
    print payment.id
except IOError as ioe:
    if isinstance(ioe, braintreehttp.HttpError):
        # Something went wrong server-side
        print ioe.status_code
        print ioe.headers["PayPal-Debug-Id"]
    else:
        # Something went wrong client side
        print ioe
```

If you're migrating from v1, check out our [Migration Guide](./docs/Migrating.md).

## Building

To try this out, update the version of `paypalrestsdk` in your `requirements.txt` to `2.0.0rc2`:

Please feel free to create an issue in this repo with any feedback, questions, or concerns you have.

## Running tests

To run integration tests using your client id and secret, clone this repository and run the following command:
```sh
$ pip install nose # if not already installed
$ PAYPAL_CLIENT_ID=your_client_id PAYPAL_CLIENT_SECRET=your_client_secret nosetests --exe
```

You may use the client id and secret above for demonstration purposes.


*NOTE*: This API is still in beta, is subject to change, and should not be used in production.

