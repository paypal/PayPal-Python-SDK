import re
from pydoc import locate
import paypalrestsdk
import inspect

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


def join_url(url, *paths):
    """
    Joins individual URL strings together, and returns a single string.

    Note: works only with paths that don't end in a trailing slash!
    join_url('v1/foo/', 'var') -> 'v1/foo/bar/bar'
    https://docs.python.org/3.7/library/re.html#re.sub
    Changed in version 3.7: Empty matches for the pattern are replaced when adjacent to a previous non-empty match.
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
    klass = locate(resource_class_dict[name.lower()])
    return klass
