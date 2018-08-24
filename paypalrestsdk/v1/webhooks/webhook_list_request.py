# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# webhook_list_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/7xX32/bNhB+319xYPcQF7KVDWvX+c1I0iVY1niJsz0YxnSWzhYbilRJKq5R5H8fjpRdy27aYQvylPATf3zffbzj+ZN4hxWJoVjRvDTmbqCk8yIRp+RyK2svjRZDcSmdd4BKQTvNwcJYQA1Y1wORiD8asusxWqzIk3ViOP0kJuuaN3beSr0UifgTrcS5ovZA1Hlp7N+eZyXiN1q3+MHhb6XiPcGX9Pl4qcPYkquNdgTzdRhn7a6yyIC0l34NfMAATmmBjfIgHWSj8fjy4mQ0ubh6lzH5kbW4jmyPE3FNWFxptRbDBSpHDHxopKViC4ytqcl6SU4MdaPUwywR54QF2U4EZol4a2y1j43Rl/sYH0HORw68JUNRWcS20fwrBgBam/Zi+vVAsotgFtsg/l/t031Wh4Q2R3WI7YBdgiMNyHy+QvL1fyd5dk/awyTetz2exN/CXexS7eKPs21q8AY8aQgrHI9WpcxL/sc1c143J1ibxm6UDWCy+8mbkF/tcqlz1RRSL0HTagNiyIE1oCXAoqAiAVdTLhfx7qPzZKW7g6PsZdaDlVQF5GiLcJClWmFOMUl2VGVRQ3en7GW2t5yvW+Dnmro21lPRkkpgGr/do1Qc0BafHb3YQv0A9UMi8uTe03n6WHEpdpza9bOL7/kJZVOh7lvCIijZmcwec2SCkiepGck3NWj+s0u+BbqsJyVBo+WHpiUHPOuZGDqPvukmzBY6ZBk/cSRxkwNPGM/Zv+Ariw7XMDzkeXG6cXuTqU8bzUup72DnWLiav6f8C9VcSb1XOTfI44XIxpekb0khZ+n0fDQ5uxrdQFg6O0oLk7sUa5mW6Mmg64cP6TPkZGlp0VHTAocO5KaqFXkCj3ZJHm6vL0MVqvCO2mc/qstRqYSnz6WOXyrypSlgJX0JvpQu6E64XZjeXl+Ap6rmpdy+VOhnR6X3tRumqTdGuYEkvxgYu0xLX6nULvLXr34+7g3gIpTjtnp+nyWQHWUJoC4g62WQl2gxDz0Kd0W1pX5tTU7OSb0cACvKWGvG3QdvcUdr2PjCWo3mxPUl+mgT4DYEUWPUg+G5YIO1D/AzpXmMace6LXRo3vlkMt7YYNvT+XX7onnPpMCS6tCP40PuUw5/JMiJyS/WN6/Iq1/evHnhKOcV/Z96SfvuO7L3FN5s1FxSQr8c7I1GNxqruVw2pnFq3T41c4r3w1GF2svcbQoRLxvADRFMQ/W4bhm6z+xWq9VAosbADZ2TS13xQ5zy2v5G0v5w8JFl9J6tAje2a0QcHxpxe30ZwyQd5EYv5LJprxE3EKTBaMiUyVGVxvksRFfq3FTcMmXjq5tJBtp4uZB5tLIi53AZ4ouet/Qo22YNpI7VQBr9RIGYPSTixGhPuu3pBda1armk713oPs69r3+PeTQUv55NRPxtIIYivf8h3WXv0p2W+exjTbmn4iY8pyemIDH88fj44bt/AAAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhookListRequest:
    """
    Lists all webhooks for an app.
    """
    def __init__(self):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks?"
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    def anchor_type(self, anchor_type):
        params = str(anchor_type)
        self.path += "anchor_type=" + quote(params) + "&"
        return self

    
