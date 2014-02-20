from distutils.core import setup

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'paypalrestsdk'))
from version import __version__

setup(
  name='paypalrestsdk',
  version= __version__,
  author='PayPal',
  author_email='DL-PP-Platform-Python-SDK@ebay.com',
  packages=['paypalrestsdk'],
  scripts=[],
  url='https://developer.paypal.com',
  license='PayPal SDK License',
  description='The PayPal REST SDK provides Python APIs to create, process and manage payment',
  long_description="""
    The PayPal REST SDK provides Python APIs to create, process and manage payment.

    1. https://github.com/paypal/rest-api-sdk-python/ - README and Samples
    2. https://developer.paypal.com/webapps/developer/docs/api/ - API Reference
  """,
  install_requires=['requests'],
  classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Topic :: Software Development :: Libraries :: Python Modules'
  ],
  keywords="paypal rest sdk",
)
