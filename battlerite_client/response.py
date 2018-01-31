from .constants import ACTIONS, SUCCESS_CODES
from .match import Match


class Response:
    """
    This class represents a response from Battlerite's API.
    """

    def __init__(self, action, response) -> None:
        self.raw = response
        self.action = action
        self.success = response.status_code in SUCCESS_CODES

    def parse(self):
        """
        Parses the result and creates objects for it.
        """
        if not self.success:
            return None

        if self.action == ACTIONS.MATCHES:
            return [Match(data) for data in self.raw.json()['data']]
        else:
            raise NotImplementedError()
