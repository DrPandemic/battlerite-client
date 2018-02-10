from .constants import ACTIONS, SUCCESS_CODES
from .match import Match
from .player import Player
from .team import Team


class Response:
    """
    This class represents a response from Battlerite's API.
    """

    def __init__(self, action, response) -> None:
        self.raw = response
        self.action = action
        self.success = response.status_code in SUCCESS_CODES
        self.rate_exceeded = response.status_code == 429
        self.rate_limit_limit = response.headers.get('X-RateLimit-Limit')
        self.rate_limit_remaining = response.headers.get('X-RateLimit-Remaining')
        self.rate_limit_reset =  response.headers.get('X-RateLimit-Reset')

    def parse(self):
        """
        Parses the result and creates objects for it.
        """
        if not self.success:
            return None

        if self.action == ACTIONS.MATCHES:
            complete = self.raw.json()
            return [Match(data, complete) for data in complete['data']]
        elif self.action == ACTIONS.PLAYERS:
            complete = self.raw.json()
            return [Player(data) for data in complete['data']]
        elif self.action == ACTIONS.TEAMS:
            complete = self.raw.json()
            return [Team(data, complete) for data in complete['data']]
        else:
            raise NotImplementedError()
