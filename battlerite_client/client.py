import requests
from typing import Dict
from .response import Response
from .constants import ACTIONS, BASE_URL


class Client:
    """
    This class is used to interact with Battlerite's API.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def matches(self, params: Dict = {}):
        """
        Returns matches.
        """
        return self.call(ACTIONS.MATCHES, params)

    def get_url(self, action: ACTIONS) -> str:
        """
        Returns the URL for a given action.
        """
        if action == ACTIONS.MATCHES:
            return f"{BASE_URL}/matches"
        else:
            raise NotImplementedError()

    def call(self, action: ACTIONS, params: Dict) -> Response:
        """
        Performs the API call and returns a Reponse.
        """
        headers = {
            'Accept': 'application/vnd.api+json',
            'Accept-Encoding': 'gzip',
            'Authorization': f"Bearer {self.api_key}"
        }
        url = self.get_url(action)

        if action == ACTIONS.MATCHES:
            response = Response(action, requests.get(url, headers=headers, params=params))
        else:
            raise NotImplementedError()

        return response
