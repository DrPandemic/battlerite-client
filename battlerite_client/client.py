import requests
from typing import Dict
from .response import Response
from .constants import ACTIONS, BASE_URL
from .team import Team
from .match import Match


class Client:
    """
    This class is used to interact with Battlerite's API.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def matches(self, params: Dict = {}) -> Response:
        """
        Returns matches.
        """
        return self.call(ACTIONS.MATCHES, params)

    def teams(self, season: int, player_ids: [int]) -> Response:
        """
        Returns a list of teams for given players during a season.
        """
        return self.call(ACTIONS.TEAMS,
                         {'tag[season]': season, 'tag[playerIds]': player_ids})

    def get_url(self, action: ACTIONS) -> str:
        """
        Returns the URL for a given action.
        """
        if action == ACTIONS.MATCHES:
            return f"{BASE_URL}/matches"
        elif action == ACTIONS.PLAYERS:
            return f"{BASE_URL}/players"
        elif action == ACTIONS.TEAMS:
            return f"{BASE_URL}/teams"
        else:
            raise NotImplementedError()

    def call(self, action: ACTIONS, params: Dict) -> Response:
        """
        Performs the API call and returns a Response.
        """
        headers = {
            'Accept': 'application/vnd.api+json',
            'Accept-Encoding': 'gzip',
            'Authorization': f"Bearer {self.api_key}"
        }
        url = self.get_url(action)

        if action in [ACTIONS.MATCHES, ACTIONS.TEAMS, ACTIONS.PLAYERS]:
            return Response(action,
                            requests.get(url, headers=headers, params=params))
        else:
            raise NotImplementedError()
