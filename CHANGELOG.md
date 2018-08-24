PayPal Python SDK release notes
============================

v2.0.0rc2
-------
* Update to latest Payments code.
* Support for Customer Disputes in Limited Release (API subject to change).

v2.0.0rc1
-------
* Refactor API around request/response model.

v1.13.1
-------
* Pass API instance in OpenIdConnect through to the base class.

v1.13.0
-------
* Proper formatting for CJK characters [#169](https://github.com/paypal/PayPal-Python-SDK/issues/169).
* Fix caching issues when refresh token is set [#176](https://github.com/paypal/PayPal-Python-SDK/issues/176).
* Fix decoding issues for different Python versions [#180](https://github.com/paypal/PayPal-Python-SDK/issues/180).
* Update OpenIdConnect to accept API instance [#208](https://github.com/paypal/PayPal-Python-SDK/pull/208).
* Added samples, and other minor bug fixes.

v1.12.0
-------
* Updated Invoicing APIs [145](https://github.com/paypal/PayPal-Python-SDK/pull/145).
* Fixed syntax error & pep8 formatting [#152](https://github.com/paypal/PayPal-Python-SDK/pull/152).

v1.11.7
-------
* Enabled Replace for Payment [#144](https://github.com/paypal/PayPal-Python-SDK/pull/144).

v1.11.6
-------
* Enabled Third Party Invoicing [#138](https://github.com/paypal/PayPal-Python-SDK/pull/138).
* Enabled Headers in Oauth calls [#134](https://github.com/paypal/PayPal-Python-SDK/pull/134).
* Updated requirements [#126](https://github.com/paypal/PayPal-Python-SDK/pull/126).
* Make sure the subscription start_date is in the future [#125](https://github.com/paypal/PayPal-Python-SDK/pull/125).
* Fix variable name typo in payment test [#117](https://github.com/paypal/PayPal-Python-SDK/pull/117).

v1.11.5
----
* Additional Webhook Validation Checks.

v1.11.4
----
* Change Live Mode Logging Warning to be Info level and use local logger.
  instead of root. See issue [#112](https://github.com/paypal/PayPal-Python-SDK/pull/112).

v1.11.3
----
* Update TLS warning message with [site information](https://github.com/paypal/TLS-update).

v1.11.2
----
* Check OpenSSL version is 1.0.1 or above.

v1.11.1
----
* Security test sandbox endpoint avaiable as a configuration.
* Warn if merchant server has below 1.0 version of OpenSSL.
* Update User Agent with crypto lib version.

v1.11.0
----
* Full request/response logged at DEBUG level for non production environments.
* Travis tests gets deployed on new platform.

v1.10.1
----
* Webhook cert patch.
* Support PAYPAL_AUTH_ALGO header for webhook validation.

v1.10.0
----
* Webhook certificate chain, common name and expiry validation added.
* Resource conversion syntax more pythonic.
* Endpoint configuration made more flexible for easier custom endpoints.
* __contains__ implemented on Resource object.
* Allow changing of logger level within projects.

v1.9.1
----
* Webhook default algorithm update.

v1.9.0
----
* Add Tox for unit test automation for different Python versions.
* Support PyPy.
* Sample added to demo update shipping cost during payment execution.

v1.8.0
----
* Payouts cancel feature added.
* Patch version imports.
* Merge pull #84 for crypto dependency docs.
* Google appengine workaround documented.

v1.7.1
----
* OpenSSL only imported when necessary.
* Dependency versions updated.
* Config.py added as source of all configuration information.
* Setup.py refactored to get information from config.

v1.7.0
----
* Payouts API support added.
* Complete pep8ify of tests and samples.

v1.6.2
-----
* Search transactions for billing agreements patched.
* Empty billing plan fetch issue fixed for subscription sample app.
* Travis build update.

v1.6.1
-----
* Python 3 compatibility patch for openssl crypto verify.

v1.6.0
-----
* Webhook and Webhook events creation and management supported.
* Parse webhook events and return the appropriate resource.
* Verification that webhook events are unaltered and originate from PayPal.
* Update Travis and Coveralls badges and User Agent for repo renaming.

v1.5.0
-----
* Payment Experience customizaton feature added via API for Web Profiles.

v1.4.1
-----
* Update Paypal-Client-Metadata-Id header for future payments.
* Subscription API changes for searching transactions and listing billing plans.

v1.4.0
-----
* Add Orders API support.
* Demonstrate samples for EC parameters support (improves feature gap between REST and CLASSIC payment APIs).
* Invocing record payment, record refund and qr-code support added.
* Activate method added for billing plans.
* Merged toanant's pull request for #62 fix.

v1.3.0
-----
* update saved credit card in vault.

v1.2.2
-----
* get_access_token added to api spec.
* Patches for python 3 compatibility.

v1.2.1
-----
* Patch for exceptions import issue #50.
* Patch for urlparse import issue.

v1.2.0
-----
* Subscription (Billing Plan and Billing Agreement) API supported.

v1.1.0
-----
* Invoicing API support added.
* Added tests and samples for using the invoicing api via the sdk.
* PayPal Mobile Backend sample added.

v1.0.0
-----
* Future Payments support added along with tests and samples.
* Move from httplib2 to requests.
* Improve error reporting.
* Exceptions below http layer removed.

v0.7.0
-----
* Allow multiple API object in same thread.
* Remove mutable default arguments.
* Change comments to be docstrings.
* Token creation supports unicode.
* Add unit_tests using mock and patch, separate from functional_tests.
* Optimize merge_dict.

v0.6.4
-----
* Support OpenIDConnect for sandbox environment.

v0.6.3
-----
* Added support for Reauthorization.

v0.6.2
-----
* Fixed content-type issue with generate_token API.

v0.6.1
-----
* Added support for Python 2.6.

v0.6.0
-----
* Added support for Auth and Capture APIs.

v0.5.3
-----
* Added Tokeninfo and Userinfo classes to support openid_connect.

v0.5.3
-----
* Validate token hash on every request.
* Resolved issue with builtin function(items) in Resource class.
