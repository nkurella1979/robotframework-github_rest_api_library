
__all__ = ['NoRestConnectionFound']

class GithubRestAPIClientException(Exception):
    """
    Base Exception class for RESTAPI Exceptions
    """
    def __init__(self, message, errors=None):
        super(GithubRestAPIClientException, self).__init__(message)

        self.errors = errors

class NoRestConnectionFound(GithubRestAPIClientException):
    """
    Exception class for error
    REST Connection to server is not found in the cache of connections
    """
    def __init__(self, message, errors=None):
        super(NoRestConnectionFound, self).__init__(message)

        self.errors = errors
