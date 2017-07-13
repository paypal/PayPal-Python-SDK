PayPal-Mobile-Backend
=====================

Flask application for a developer/merchant verifying payments and executing payments on behalf of customer who has consented to future payments

## Dependencies

(We strongly recommend that you set up a [virtualenv](http://www.virtualenv.org/) for this project, and you may also want to check out [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/) for convenience)

Install requirements using pip:

    pip install -r requirements.txt

## Configuration

Get your client credentials from https://developer.paypal.com/ and put them in a `paypal_config.py` file:

    $ cat paypal_config.py
    MODE = "sandbox"
    CLIENT_ID = "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM"
    CLIENT_SECRET = "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM"

## Run the server

    python merchant_server.py
    // * Running on http://0.0.0.0:8000/
    // * Restarting with reloader

## Verify a paypal payment

```bash
curl -X POST http://0.0.0.0:8000/client_responses \
     -H "Content-Type: application/json" \
     -d '{
            "response":{
                "id":"RETURNED PAYMENT ID",
                "state":"approved"
            },
            "payment":{
                "description":"PRODUCT DESCRIPTION",
                "amount":"1.50",
                "currency_code":"USD"
            },
            "response_type":"payment"
        }'
```
    
## Send authorization code for future payments

A customer_id (or user_id, email is used here) is sent to associate 
the refresh token that you obtain by exchanging the authorization code

```bash
curl -X POST http://0.0.0.0:8000/client_responses \
     -H "Content-Type: application/json" \
     -d '{
            "response_type":"authorization_code",
            "response": {
                "code": "RETURNED AUTH CODE"
            },
            "customer_id": "USER ID IN YOUR APP"
        }'
```

## Send correlation id and transaction details from device to charge customer

```bash
curl -X POST http://0.0.0.0:8000/correlations \
     -H "Content-Type: application/json" \
     -d '{
            "customer_id": "USER ID IN YOUR APP",
            "transactions": [
                {
                    "description":"PRODUCT DESCRIPTION",
                    "amount" : {
                        "currency": "USD",
                        "total": "1.34" 
                    } 
                }
            ], 
            "correlation_id": "CORRELATION ID OBTAINED VIA MOBILE SDK",
            "intent": "sale"
        }'
```
Set intent to sale for immediate payments or authorize to capture the payment
at a later time.


PEP 8
-----

All code follows the [PEP 8](http://www.python.org/dev/peps/pep-0008/) style guide, with the exception of E501, E261, and E302.
