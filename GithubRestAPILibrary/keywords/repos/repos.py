from robot.api import logger
from GithubRestAPILibrary.keywords.connection.connection import ConnectionKeywordsMixin
from GithubRestAPILibrary.utils.common.common import execute_get_request

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

        | Get All Public Repos | conn_1 |
        """
        response = execute_get_request(ConnectionKeywordsMixin.requests, connection_alias, '/repositories')

        logger.debug(response)

        return response

    @staticmethod
    def get_all_user_repos(connection_alias):
        """
        | connection_alias | An alias used to identify the rest connection |

        | Get All User Repos | conn_1 |
        """
        response = execute_get_request(ConnectionKeywordsMixin.requests, connection_alias, '/user/repos')

        logger.debug(response)

        return response

    @staticmethod
    def get_all_repos_for_org(connection_alias, org):
        """
        | connection_alias | An alias used to identify the rest connection |
        | org | organization name whose repos need to be retrieved |

        | Get All Repos For Org | conn_1 | Aruba |
        """
        response = execute_get_request(ConnectionKeywordsMixin.requests, connection_alias, '/orgs/:' + org
                                       + '/repos')

        logger.debug(response)

        return response
