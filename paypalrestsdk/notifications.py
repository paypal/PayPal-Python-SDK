from paypalrestsdk.resource import List, Find, Create, Delete, Update, Replace, Resource, Post
from paypalrestsdk.api import default as default_api
import paypalrestsdk.util as util
import binascii
from base64 import b64decode
import requests
import os
import sys


class Webhook(Create, Find, List, Delete, Replace):
    """Exposes REST endpoints for creating and managing webhooks

    Usage::

        >>> web_profile = WebProfile.find("XP-3NWU-L5YK-X5EC-6KJM")
    """
    path = "/v1/notifications/webhooks"

    def get_event_types(self, api=None):
        """Get the list of events types that are subscribed to a webhook
        """
        api = api or default_api()
        url = util.join_url(self.path, str(self['id']), 'event-types')
        return Resource(self.api.get(url), api=api)


class WebhookEvent(Find, List, Post):
    """Exposes REST endpoints for working with subscribed webhooks events
    """
    path = "/v1/notifications/webhooks-events"
    __root_cert_path = "data/DigiCertHighAssuranceEVRootCA.crt.pem"
    __intermediate_cert_path = "data/DigiCertSHA2ExtendedValidationServerCA.crt.pem"
    __cert_chain_path = [__root_cert_path, __intermediate_cert_path]

    def resend(self):
        """Specify a received webhook event-id to resend the event notification
        """
        return self.post('resend', {}, self)

    def get_resource(self):
        """Get the resource sent via the webhook event, e.g. Authorization, conveniently
         wrapped in the corresponding paypalrestsdk class
        """
        webhook_resource_type = self.resource_type
        klass = util.get_member(webhook_resource_type)
        resource = klass(self.resource.__dict__)
        return resource

    @staticmethod
    def _get_expected_sig(transmission_id, timestamp, webhook_id, event_body):
        """Get the input string to generate the HMAC signature
        """
        if sys.version_info[0] == 2:
            data = str(binascii.crc32(event_body.decode('utf-8').encode('utf-8')) & 0xffffffff)
        else:
            data = str(binascii.crc32(event_body.encode('utf-8')) & 0xffffffff)
        expected_sig = transmission_id + "|" + timestamp + "|" + webhook_id + "|" + data
        return expected_sig

    @staticmethod
    def _is_common_name_valid(cert):
        """Check that the common name in the certificate refers to paypal"""
        from OpenSSL import crypto
        if cert.get_subject().commonName.lower().endswith(".paypal.com"):
            return True
        else:
            return False

    @classmethod
    def _get_certificate_store(cls):
        """Returns a certificate store with the trust chain loaded
        """
        from OpenSSL import crypto
        store = crypto.X509Store()
        try:
            for cert_path in cls.__cert_chain_path:
                cert_str = open(os.path.join(os.path.dirname(__file__), cert_path)).read()
                cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_str)
                store.add_cert(cert)
            return store
        except Exception as e:
            print(e)

    @classmethod
    def _verify_certificate_chain(cls, cert):
        """Verify certificate using chain of trust shipped with sdk
        """
        from OpenSSL import crypto
        store = cls._get_certificate_store()
        try:
            store_ctx = crypto.X509StoreContext(store, cert)
            store_ctx.verify_certificate()
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def _verify_certificate(cls, cert):
        """Verify that certificate is unexpired, has valid common name and is trustworthy
        """
        if cls._verify_certificate_chain(cert) and cls._is_common_name_valid(cert) and not cert.has_expired():
            return True
        else:
            return False

    @staticmethod
    def _get_cert(cert_url):
        """Fetches the paypal certificate used to sign the webhook event payload
        """
        from OpenSSL import crypto
        try:
            r = requests.get(cert_url)
            cert = crypto.load_certificate(crypto.FILETYPE_PEM, str(r.text))
            return cert
        except requests.exceptions.RequestException as e:
            print("Error retrieving PayPal certificate with url " + cert_url)
            print(e)

    @classmethod
    def _verify_signature(cls, transmission_id, timestamp, webhook_id, event_body, cert, actual_sig, auth_algo):
        """Verify that the webhook payload received is from PayPal,
        unaltered and targeted towards correct recipient
        """
        from OpenSSL import crypto
        expected_sig = WebhookEvent._get_expected_sig(transmission_id, timestamp, webhook_id, event_body)
        try:
            crypto.verify(cert, b64decode(actual_sig), expected_sig.encode('utf-8'), auth_algo)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def verify(cls, transmission_id, timestamp, webhook_id, event_body, cert_url, actual_sig, auth_algo='sha256'):
        """Verify certificate and payload
        """
        __auth_algo_map = {
            'SHA256withRSA': 'sha256WithRSAEncryption',
            'SHA1withRSA': 'sha1WithRSAEncryption'
        }
        try:
            if auth_algo != 'sha256' and auth_algo not in __auth_algo_map.values():
                auth_algo = __auth_algo_map[auth_algo]
        except KeyError as e:
            print('Authorization algorithm mapping not found in verify method.')
            return False
        cert = WebhookEvent._get_cert(cert_url)
        return WebhookEvent._verify_certificate(cert) and WebhookEvent._verify_signature(transmission_id, timestamp, webhook_id, event_body, cert, actual_sig, auth_algo)


class WebhookEventType(List):
    """Exposes REST endpoint for listing available event types for webhooks
    """
    path = "/v1/notifications/webhooks-event-types"
