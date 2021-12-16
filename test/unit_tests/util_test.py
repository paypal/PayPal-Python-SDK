import paypalrestsdk.util as util
from paypalrestsdk.payments import Authorization
import unittest


class TestUtil(unittest.TestCase):

    def test_join_url(self):
        url = util.join_url("payment", "1")
        self.assertEqual(url, "payment/1")
        url = util.join_url("payment", "/1")
        self.assertEqual(url, "payment/1")
        # as of Python 3.7 this won't work
        # url = util.join_url("payment/", "1")
        # self.assertEqual(url, "payment/1")
        # url = util.join_url("payment/", "/1")
        # self.assertEqual(url, "payment/1")

    def test_join_url_params(self):
        url = util.join_url_params("payment", {"count": 1})
        self.assertEqual(url, "payment?count=1")
        url = util.join_url_params("payment", {"count": 1, "next_id": 4321})
        self.assertTrue(
            url in ("payment?count=1&next_id=4321", "payment?next_id=4321&count=1"))

    def test_get_member(self):
        klass = util.get_member('authorization')
        self.assertEqual(klass, Authorization)
