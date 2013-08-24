

class ConnectionError(Exception):
    def __init__(self, response, content=None, message=None):
        self.response = response
        self.content = content
        self.message = message

    def __str__(self):
        message = "Failed."
        if hasattr(self.response, 'status'):
            message = message + "  Response status = %s." % (self.response.status)
        if hasattr(self.response, 'reason'):
            message = message + "  Response message = %s." % (self.response.reason)
        return message


# Raised when a Timeout::Error occurs.
class TimeoutError(ConnectionError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# Raised when a OpenSSL::SSL::SSLError occurs.
class SSLError(ConnectionError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# 3xx Redirection
class Redirection(ConnectionError):
    def __str__(self):
        message = super(Redirection, self).__str__()
        if self.response.get('Location'):
            message = "%s => %s" % (message, self.response.get('Location'))
        return message


class MissingParam(TypeError):
    pass


class MissingConfig(Exception):
    pass


# 4xx Client Error
class ClientError(ConnectionError):
    pass


# 400 Bad Request
class BadRequest(ClientError):
    pass


# 401 Unauthorized
class UnauthorizedAccess(ClientError):
    pass


# 403 Forbidden
class ForbiddenAccess(ClientError):
    pass


# 404 Not Found
class ResourceNotFound(ClientError):
    pass


# 409 Conflict
class ResourceConflict(ClientError):
    pass


# 410 Gone
class ResourceGone(ClientError):
    pass


# 5xx Server Error
class ServerError(ConnectionError):
    pass


# 405 Method Not Allowed
class MethodNotAllowed(ClientError):

    def allowed_methods(self):
        return self.response['Allow']
