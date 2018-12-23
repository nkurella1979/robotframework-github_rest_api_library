from GithubRestAPILibrary.utils.common.constants import RESPONSE_OK_STATUS_CODE

def execute_get_request(request, connection_alias, uri):
    response = request.get_request(connection_alias, uri)
    if response.status_code != RESPONSE_OK_STATUS_CODE:
        raise InvalidResponseStatusCodeError("Expected response code: %s actual response code: %s"
                                             %(RESPONSE_OK_STATUS_CODE, response.status_code))

    return response
