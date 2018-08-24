# This class was generated on Mon, 29 Jan 2018 15:08:23 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# template_delete_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/2SQQW/iMBCF7/srrHe2CLtH31YkK9DutrRFvVSoMvFAXDm2a09QI8R/r9JARen109PM994BN7olKDC10WmmiSFHTJAoKdfJRrbBQ6H8wFlocU5KsenFopxA4q6j1C910i0xpQz1tJaYkzaUrumfkNprttTcfGEHrPo4WGVO1u8g8aiT1RtHV7bP1kDiL/Un/k171ZBYlCJsBTf0qS44iLHnYP87Jd2PD6cS96TNrXc91Fa7TAN47WwiA8WpI4llCpESW8pQvnPuuB4zlHk8MsAB5Rh8pks2C57Jn2LQMTpb68G0eMnBQ2LOHP8TN8EMk1f/qlWFcR8oFPufhfX7YGvrd8W5Sy4OF2scIVG9RaqZzANr7vIsGIL6NZ0ef7wDAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class TemplateDeleteRequest:
    """
    Deletes a template, by ID.
    """
    def __init__(self, template_id):
        self.verb = "DELETE"
        self.path = "/v1/invoicing/templates/{template_id}?".replace("{template_id}", quote(str(template_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
