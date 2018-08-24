# This class was generated on Mon, 29 Jan 2018 15:08:22 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# userinfo_get_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/8RYUXMTNxB+76/YUR/6crENffNbJoGSKYEUAjOZlrFlac+nopMOaS9wMPz3jqSzOfmSkE7T4yWxvl3pvv0krVb6wl7wGtmStR6dMqWdbZFYwU7RC6caUtawJXtd2Y8eggtIJK60n/3VLha/io224v2H1hLGdvorPDlrtgl5YQmXCZ4PcbislIfjizNQHiQ2DgUnlDN44xHW14/mlrdUPZ6TfY9mvmO3BmU8IZf99+eHBFjB/mjRdRfc8RoJnWfLP7+wy64JQXpyymxZwd5yp/hGYx+8FxXWnBXsd+x6aKTBU6XDcEAVgkPfWOMRNh1wSL3hmusWZ/CWayVTI4S2tg0aJdczVrBj53iXqCwK9gq5fGl0x5Yl1x4D8KFVDiVbkmuxYBfONuhIoWdL02r99V3BniGX6LLo3hXsqXX1IXbBqTrEwhfQU6IQhgxQCiVhe6WC4Kug+Fisu2V62aCBs1M4scagoLRowkCu5sFlJq1oazQUW8+Veb+siJrlfJ6EmhmkuW9Q+B44Emmkow33Shw9Wi1mFdX659fEjeROnmiuav9v1O2BobzfXyJcCNsaWlFwGypwYMjVODaApq3RxWjBlnH59F0gdPGz/0g9rowinzgupUPvb4hibxgEsMdy7pcVAhoZZ/AXD43DEp1DCX2H2f+ueVTJdRnbb9iYbW97YEVvY6et4FpRTm8A3sBPUQfWwc5pIqKN9cT1SliZr9wcH9P9rBoIxkA5+cbmRKwdbgOVIeE9NObqiRMW0Dh7rYyIv7BEQa3DIvBPXSei7skh0uqmzTYyjUMpW60h+e23GpxwA8oI3UqMKaSyrUcwbb1BB9zIXQfD64eZoHf3iJNvceW42R4kxAE6jm6X+yqrZcwrfIsQ3SeanI1yVElOOekhemca7B27ApSB9dXV1dXR+fnR6eka0hE3g9ChQ+7g/PgKNgjrxWKxWBfwsVKiAmWkCpVOKCQ4xbmMzsqDrRXFEujSggsVkUdDYI3u9m5FoBFb8dP7j04jHdZc6Uy2HXLPkwOPgv9DHSAHrDfWauTmFtqra3SqVCjH/IemPJCz/WR9rJAqdFH6QWg4jCfM4W6oiWak5LXS3Srs+iyuHL8hXbYu2GJq1NynvBEa4b8vdoXKLtKJotmikeiyQPbQnSsseU3FUl2jGUuewWO20Rz1LpXzVOSK/yDBYyGC4wLmu1kweU3EslZSahwrnuNjvsneC/1D9B1RvpXrQNt4/kfSyoBUvtG8C2PGXN8XAcpsge/cGu7Iz+DCeq82utvVCR5IkUafyoO2LNUn9OCto1DDC2FdHIbsYVJLkxu7pdSNRjz4PeXWYpV34eaZp+kBOJbu7PTwXhXdp+JbWYOrVIjlnHPDPU9IQo2xZ1/bTRWFiqVyHsAeG3N/8+r54ZaKYdhSaYS+51TVdrvJS+zYvunM2/yNgsJ6KW1+kkNfiSnv28k0T08s+UL/ht21ziehfWs5tStxVv12ywK4wTiOZOe037Dh9tZOlWE+W4P9y9Y33gPwzp1KqkYIzg91yWIn1hCa/k2OsYI9I2rOkSor2ZL99uSSpbc8tmTz60dzJdGQoq5/Hesfx/YPpKxgTz41KAjl6yjqSbjdLx8vFl9/+gcAAP//
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class UserinfoGetRequest:
    """
    Shows user details.<blockquote><strong>Note:</strong> This API is deprecated. Use `v1/oauth2/token/userinfo` instead.</blockquote>
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/identity/openidconnect/userinfo?"
        self.headers = {}
        self.body = None

    def schema(self, schema):
        params = str(schema)
        self.path += "schema=" + quote(params) + "&"
        return self

    
