from robot.api import logger
from GithubRestAPILibrary.keywords.connection.connection import ConnectionKeywordsMixin
from GithubRestAPILibrary.keywords.repos.repos import ReposKeywordsMixin

# pylint: disable=too-many-ancestors
__version__ = "1.0.0"

__all__ = ['GithubRestAPILibrary']

class GithubRestAPILibrary(ConnectionKeywordsMixin,
                           ReposKeywordsMixin):
    """
    Robot Framework GitHubRestAPI Keyword Library.

    All the keywords pertaining to GithubRestAPI are
    exposed to the user through this library.

    The Library is derrived from below libraries
    each of which is a place holder for the respective
    networker component keywords.

    | ConnectionsKeywordsMixin | keywords specific to REST Connections |
    | ReposKeywordsMixin | keywords specific to RESP API Repos |

    This library should have any keywords common to all libraries.
    """
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        """
        Framework init

        """
        pass
