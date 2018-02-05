from .constants import ACTIONS, SUCCESS_CODES
from .match import Match
from .team import Team


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
            complete = self.raw.json()
            return [Match(data, complete) for data in complete['data']]
        elif self.action == ACTIONS.TEAMS:
            complete = self.raw.json()
            return [Team(data, complete) for data in complete['data']]
        else:
            raise NotImplementedError()
