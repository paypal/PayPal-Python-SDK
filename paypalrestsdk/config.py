__version__ = "2.0.0rc2"
__pypi_username__ = "paypal"
__pypi_packagename__ = "paypalrestsdk"
__github_username__ = "paypal"
__github_reponame__ = "PayPal-Python-SDK"

import re
import os

def find_packages():
    path = "."
    ret = []
    for root, dirs, files in os.walk(path):
        if '__init__.py' in files:
            ret.append(re.sub('^[^A-z0-9_]+', '', root.replace('/', '.')))
    return ret
