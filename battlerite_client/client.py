import requests
from .response import Response
from .constants import ACTIONS, BASE_URL


class Client:
    """
    This class is used to interact with Battlerite's API.
    """

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_url(self, action: ACTIONS) -> str:
        """
        Returns the URL for a given action.
        """
        if action == ACTIONS.MATCHES:
            return f"{BASE_URL}/matches"
        elif action == ACTIONS.PLAYERS:
            return f"{BASE_URL}/players"
        else:
            raise NotImplementedError()

    def call(self, action: ACTIONS) -> Response:
        """
        Performs the API call and returns a Response.
        """
        headers = {
            'Accept': 'application/vnd.api+json',
            'Accept-Encoding': 'gzip',
            'Authorization': f"Bearer {self.api_key}"
        }
        url = self.get_url(action)

        if action == ACTIONS.MATCHES:
            response = Response(action, requests.get(url, headers=headers))
        elif action == ACTIONS.PLAYERS:
            response = Response(action, requests.get(url, headers=headers))
        else:
            raise NotImplementedError()

        return response
