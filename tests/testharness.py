import unittest

from paypalrestsdk.core.environment import SandboxEnvironment
from paypalrestsdk.core.paypal_http_client import PayPalHttpClient
import os

class TestHarness(unittest.TestCase):

    def setUp(self):
        self.environment = SandboxEnvironment(os.getenv("PAYPAL_CLIENT_ID"), os.getenv("PAYPAL_CLIENT_SECRET"))
        self.client = PayPalHttpClient(self.environment)
