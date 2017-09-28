import re
from pydoc import locate
import paypalrestsdk
import inspect

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

CLASS_MAPPING_TABLE = {
    'payouts_item': 'paypalrestsdk.payments.PayoutItem',
    'payouts': 'paypalrestsdk.payments.Payout',
    'plan': 'paypalrestsdk.payments.BillingPlan',
    'agreement': 'paypalrestsdk.payments.BillingAgreement',
    'invoices': 'paypalrestsdk.invoices.Invoice',
    'dispute': 'paypalrestsdk.resource.Resource',  # not mapped ?
    'authorization_consent_revoked': 'paypalrestsdk.resource.Resource',  # not mapped ?
    'merchant-onboarding': 'paypalrestsdk.resource.Resource',  # not mapped ?
    'partner-consent': 'paypalrestsdk.resource.Resource',  # not mapped ?
    'vault-credit-card': 'paypalrestsdk.resource.Resource'  # not mapped ?
}


def join_url(url, *paths):
    """
    Joins individual URL strings together, and returns a single string.

    Usage::

        >>> util.join_url("example.com", "index.html")
        'example.com/index.html'
    """
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def join_url_params(url, params):
    """Constructs percent-encoded query string from given parms dictionary
     and appends to given url

    Usage::

        >>> util.join_url_params("example.com/index.html", {"page-id": 2, "Company": "Pay Pal"})
        example.com/index.html?page-id=2&Company=Pay+Pal
    """
    return url + "?" + urlencode(params)


def merge_dict(data, *override):
    """
    Merges any number of dictionaries together, and returns a single dictionary

    Usage::

        >>> util.merge_dict({"foo": "bar"}, {1: 2}, {"Pay": "Pal"})
        {1: 2, 'foo': 'bar', 'Pay': 'Pal'}
    """
    result = {}
    for current_dict in (data,) + override:
        result.update(current_dict)
    return result


def older_than_27():
    import sys
    return True if sys.version_info[:2] < (2, 7) else False


def get_member(name):
    """
    Get the paypalrestsdk member class represented by name. Helper
    method for fetching resource sent via webhook event

    Usage::

    >>> util.get_member('authorization')
    <class 'paypalrestsdk.payments.Authorization'>
    """
    resource_class_dict = dict((k.lower(), ("{0}.{1}".format(v.__module__, k)))
                               for k, v in inspect.getmembers(paypalrestsdk, inspect.isclass))
    try:
        klass = locate(resource_class_dict[name.lower()])
    except:
        klass = locate(CLASS_MAPPING_TABLE[name.lower()])
    return klass
