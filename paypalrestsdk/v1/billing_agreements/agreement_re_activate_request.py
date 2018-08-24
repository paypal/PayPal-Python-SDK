# This class was generated on Mon, 29 Jan 2018 15:08:22 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# agreement_re_activate_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/6RUwW7bMAy97ysInt24G3byLWg2NBvWZE2wy1CktMXEKhzJpehuRpB/Hxy7TuIAHYZdbOiJIvneo7TDO9oyJkgbYd6y05HwFWVqX0gZI5xwyMSWar3DBO+PewEIQhVKdoYNpLYorNtAnyaCtIbpZARTB5ozfFnM7kD4ueKgkHpTR2BdVlSGgRw89udWQUl5ZbqyXh7Bp0+cKfyymrcfAueVQXNSaANTDocqwhS8g7WXbvnarvUOyJkD2tcC2vqq+TkDWSXCLqtHGOH3iqWek9CWlSVg8vMhwlsmwzJEP3vZDrE5aX6G7XBZl43IQcW6DUb4g8RSWvBQ/JU1GOFXrruNCwOWOcN0An49YKL+hCw3JMYiVLd1ryO8ZzIzV9SYrKkI3ADPlRU2mKhUHOFcfMmilgMmriqK/UMbw0HbJD2JcV900VgFk96qt4gNbT2j+WbYuQBjMMf1qw6teQqH0xfi/JMaHXAqx9/9a8bxjFAHXHo3GNCjgW3rWU5uw//bcOvfvokKpXeB2zwNHOGNd8quMxWpLAubHe5H/BS8wwhvVctvrLk3mOB8tlhiO9KYYPzyPi6pbhoOcXflr3oOId6dDvI+Pn9JPv0uOVM2zdRU4cYbxuTD9cf9uz8AAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class AgreementReActivateRequest:
    """
    Re-activates a suspended billing agreement, by ID. In the JSON request body, include an `agreement_state_descriptor` object with with a note that describes the reason for the re-activation and the agreement amount and currency.
    """
    def __init__(self, agreement_id):
        self.verb = "POST"
        self.path = "/v1/payments/billing-agreements/{agreement_id}/re-activate?".replace("{agreement_id}", quote(str(agreement_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
    
    def request_body(self, agreement_state_descriptor):
        self.body = agreement_state_descriptor
        return self
