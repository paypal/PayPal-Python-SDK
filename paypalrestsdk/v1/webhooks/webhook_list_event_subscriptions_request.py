# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# webhook_list_event_subscriptions_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/7yUTW/TQBCG7/yK1Zy3deDAwbeqCbTiK0DEpYqiSTzBC86uuzNusSL/d7S2E7wxUPGhniK/Ga+eZ/zae3iLO4IU7mmdO/f1vDAsK7ojKyuu1rzxphTjLIOGKR0vIYXXhoVVO6miSbV1XqHqD9RqXavr6TloeF+Rr+focUdCniG9WWq4IszIn6YvnN+dZnOUPMr2sKjLwM7ijf0MGj6hN7guKHZamQw0vKK6j0cqi5zU9VS5rZKcDuCtxn1uNrkSp8JaYs1gdOE91h3ERMMHwuydLWpIt1gwheC2Mp4ySMVXpGHuXUleDDGktiqKZtnNEEt3SAhDxKWzTF12tJy1qw4XKux+rPt7yXBPUDzotU/uzyz6YKhx8xO8MVnXJ6lL4ggyzmPeC6swgD3I/PzvmX9VnGxAMuSN8xNelVc7tGeeMAtHqcHwoVot/7+uvG2OftDBhp8hfB+Mq19Zc1v1cCpMPRIhC0oVF+IYjSm7v8ImMe7Df6FdNstGw6WzQrZ/GQHLsjAbDAzJF24f+ZVI+YYkdxmk8HK2gO6zBCkkd08T68Rs+zs46SE52f/4DjVJi3x2qPzsW0kboexjK3fpMoL02WTSPPkOAAD//w==
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class WebhookListEventSubscriptionsRequest:
    """
    Lists event subscriptions for a webhook, by ID.
    """
    def __init__(self, webhook_id):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks/{webhook_id}/event-types?".replace("{webhook_id}", quote(str(webhook_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
