import logging
import os
import re
import unittest

import paypalrestsdk as paypal

# Logging
logging.basicConfig(level=logging.INFO)

# Credential
client_id     = "EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM"
client_secret = "EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM"

# Set credential for default api
paypal.configure( client_id= client_id, client_secret= client_secret )

def assert_regex_matches(test, s, regex):
    test.assertTrue(re.compile(regex).search(s))

