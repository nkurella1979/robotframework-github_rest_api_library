from robot.api import logger
from GithubRestAPILibrary.keywords.connection.connection import ConnectionKeywordsMixin

# pylint: disable=too-many-ancestors

__version__ = "1.0.0"

class ReposKeywordsMixin(object):
    """
    This class provides the mechanism to get repos details
    """

    @staticmethod
    def get_all_public_repos(connection_alias):
        """
        | connection_alias | An alias used to identify the rest connection |
        """
        response = ConnectionKeywordsMixin.requests.get_request(connection_alias, '/repositories')

        logger.debug(response)
