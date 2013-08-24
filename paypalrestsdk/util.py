import re
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode


# Join given url
# == Example
#   api.join_url("example.com", "index.html") # Return "example.com/index.html"
def join_url(url, *paths):
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url


def join_url_params(url, params):
    return url + "?" + urlencode(params)


# Merge dict
def merge_dict(data, *override):
    dict_list = list(data.items())
    for value in override:
        dict_list = dict_list + list(value.items())
    return dict(dict_list)
