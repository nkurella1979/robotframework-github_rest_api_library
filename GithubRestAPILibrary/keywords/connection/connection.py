from robot.api import logger
from RequestsLibrary.RequestsKeywords import RequestsKeywords
from GithubRestAPILibrary.keywords.connection.constants import (
    DEFAULT_GITHUB_REST_SERVER_PORT,
    DEFAULT_DEBUG,
    DEFAULT_VERIFY,
    DEFAULT_MAX_RETRIES,
    DEFAULT_BACKOFF_FACTOR,
    DEFAULT_DISABLE_WARNINGS
)
from GithubRestAPILibrary.errors.connection.connection import (
    NoRestConnectionFound
)
# pylint: disable=too-many-ancestors

__version__ = "1.0.0"

class ConnectionKeywordsMixin(object):
    """
    This class provides the mechanism to create REST connections,
    store and retrieve them.
    """
    requests = RequestsKeywords()

    @staticmethod
    def open_rest_connection(user,
                             passwd,
                             url,
                             connection_alias,
                             headers={},
                             cookies={},
                             auth=None,
                             timeout=None,
                             proxies=None,
                             verify=DEFAULT_VERIFY,
                             debug=DEFAULT_DEBUG,
                             max_retries=DEFAULT_MAX_RETRIES,
                             backoff_factor=DEFAULT_BACKOFF_FACTOR,
                             disable_warnings=DEFAULT_DISABLE_WARNINGS
                            ):
        """
        Open a REST Connection to the given server

        | user | username to connect to Networker REST API |
        | passwd | password to connect to Networker REST API |
        | url | Base url of the server |
        | connection_alias | An alias used to identify this rest connection |
        """
        logger.debug("Opening REST connection to url "
                     "%s connection alias %s" %(url,
                                                connection_alias) +
                     " user %s password %s" %(user, passwd))

        ConnectionKeywordsMixin.requests.\
                create_session(
                    connection_alias,
                    url,
                    headers,
                    cookies,
                    auth,
                    timeout,
                    proxies,
                    verify,
                    debug,
                    max_retries,
                    backoff_factor,
                    disable_warnings)


    @staticmethod
    def switch_rest_connection(connection_alias):
        """
        Switches REST Connection to the specified connection alias
        for the given url

        | connection_alias | An alias used to identify this rest connection |
        """
        try:
            session = ConnectionKeywordsMixin.requests._cache.switch(connection_alias)
        except KeyError:
            raise NoRestConnectionFound("REST Connection "
                                        " to connection with alias %s does not exist"
                                        %(connection_alias))
        return session
