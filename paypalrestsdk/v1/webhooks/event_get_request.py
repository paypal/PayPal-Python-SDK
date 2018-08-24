# This class was generated on Mon, 29 Jan 2018 15:08:26 PST by version 0.1.0-dev+6beb51-dirty of Braintree SDK Generator
# event_get_request.py
# @version 0.1.0-dev+6beb51-dirty
# @type request
# @data H4sIAAAAAAAC/8yXT1PjRhPG7++n6Jo3B6iSJRIC2fWNWthAZRMIeHOhqHVbaluzSDPKdAvjUHz31GgkY1sLbBKK5KieP+5fPzPPtO/UL1iSGiq6ISPxjERF6pA4dboSbY0aqovczhkyEtQFw9Q6QJjTJLf2GppVYKzoqU7RL4hgsoCTw1hF6tea3OIMHZYk5FgNL68idUyYkduMvreu3IydoeRrsTs1WlQ+VxanzUxF6jd0GicFrTJ80pmK1E+0aIM9nlFOcHIIdgqS0xMkDeo812kOYoFzO++K4OEOnMNFyGcnUueE2akpFmo4xYLJB36vtaNMDcXVFKkzZytyoonV0NRFcX8V5hBL2MQHfYgra5hCbAl85JPr8z7NefAE218iaAOrCM9rkTpCoU+iS1pLcz3eVyZDIUCTgZ8B85zMczLNkSHsmkWgDVyeGCFnSDb2mlpXolxt5SIVD5NErC041iTT2LpZkktZJG6a7u7uvv0/U+r3HuzF+9v/tFaN3NFXHl7xk1brtRbulyvUQ3IUEKdnM3KUPVOwV+W5Icc+2z7Sw8hjVO0Mr+kq0b/AsmEpzeffM5UXTviDNtewkgmcTj5T+gWrKLS55jWILrJhGgbQp+dJXPCngaPCXy64PD4YHZ0eXECz9GoryWzKCVY6yVHIIg+agc0Ls//y5pI7mq7BtIG+Jqktq4KEQNDNSODj+YcYRhZKvKZGqg4uxaKI/PSJNmGkJMltBnMtOUiuucEODvPx/ASEysov/Vpf2d/7YWc7hhOTFnUWfmH8zTiC8dY4akxqvD2GNEeHqX/vmtencjSonE2JWZtZDJ5o7FnHoLnZ4poW0MniWa1Z+kEjBuCyBIEx8CBwPWGvr5Em/EoXKdR0TbplqC/e8Wh01sng2l/3b/EXxXslAkfFWvrhu5/7pS9/SNDfS2/gzx6Rvbdv3iyfnu+3o7b7YHI3xIAMaLzJhBas2b8RujZYTvSstjUXC8iaVCYUzgdTiUZ0yp01+WUxXBDBZWMe522G/JDdfD6PNRpsckNmPTMlGeHErx10SJuf8a3HeJnX8mpFCPuIozliW7uUNtRYBvuSdIP/yeeyS67fAWyO9MEMltTpu4Ts7obYR1/PQPtKgFyXJbrFGtpDbLN1bUfa01wt+3FZdgdrGsF764Bu0TtdBOMDqHDhzyxgLbl1+o9eqxiPX+igqnfWCJm2jVdYVUWbVfKZm/7mWKT6ObjcUP14NFLhv40aquTm22SVg5NWJh40kJzcdf9p7lWkjm4rSoWyC0Gp+Z3NSA2/29m5/9+fAAAA//8=
# DO NOT EDIT
import braintreehttp

try:
    from urllib import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

class EventGetRequest:
    """
    Shows details for a webhook event notification, by ID.
    """
    def __init__(self, event_id):
        self.verb = "GET"
        self.path = "/v1/notifications/webhooks-events/{event_id}?".replace("{event_id}", quote(str(event_id)))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"
        self.body = None

    
