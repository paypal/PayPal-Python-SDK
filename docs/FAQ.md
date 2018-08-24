# FAQ

## Q. Why did we create a new SDK that is different than 1.x ?
> We released 1.0 back in January 2015. In almost 2 years, we have made some big improvements to SDK, mostly derived from feature requests from developers like you. We tried to add all those features as much as we could, but few remained far fetched as they were breaking our current integration. All these issues will be fixed in 2.x. That required us to make some tiny breaking changes, but opens up a plethora of features that otherwise were inaccessible.
For e.g. 
- **Retries** are currently not working as expected. Developers are not allowed to have full control over retry logic.
- **[PayPal-Request-Id](https://developer.paypal.com/docs/api/auth-headers/)** are auto-generated internally and are not working as expected. Developer can set a requestId but is not handled correctly, if you were to make the same call again yourself.
- **HTTPClient** is not accessible for advanced users who wish to use their own implementation for making calls to PayPal.
- **PayPal-Debug-Id** from a response is almost impossible to access. This id is used by PayPal to relate internal logs in case of any issues.    

## Q. What do I need to do to migrate from 1.x to 2.x?
> You can follow our steps mentioned in [our migration guide](./Migrating.md).

## Q. What is PayPal-Request-ID and should I use it? How?
> As mentioned in our [developer docs](https://developer.paypal.com/docs/api/auth-headers/), `PayPal-Request-ID` contains a unique ID that you generate that can be used for enforcing idempotency. Omitting this header increases the risk of duplicate transactions. 

> Using it is pretty simple. Just add a header to your request object as shown below:
```py
    request = PaymentCreateRequest()
    request.headers["PayPal-Request-ID"] = "abcd-request-id"
```

## Q. How will I retry in 2.x?
> NOTE: We highly recommend using a request id as shown above when performing retries, to prevent duplicate transactions.
> Retries are now much more simple. If your request fails for some reason and you want to try again, just resubmit the same HttpRequest object.

```py
import paypalrestsdk.core as paypal
import paypalrestsdk.v1.payments as payments

client_id = "AYSq3RDGsmBLJE-otTkBtM-jBRd1TCQwFf9RGfwddNXWz0uFU9ztymylOhRS"
client_secret = "EGnHDxD_qRPdaLdZz8iCr8N7_MzF-YHPTkjs6NKYQvQSBngp4PTTVWkPZRbL"
env = paypal.environment.SandboxEnvironment(client_id, client_secret)

client = paypal.paypal_http_client.PayPalHttpClient(environment=env)

retry = 0
result = None

request = payments.PaymentCreateRequest()
request.headers['PayPal-Request-ID'] = "abcd-request-id"
request.request_body({ ... })

while not result and retry < 3:
    try:
        result = client.execute(request).result
        print result.id
    except IOError as ioe:
        print ioe
    finally:
        retry += 1
```
