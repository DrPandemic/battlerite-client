from enum import Enum
import requests

ACTIONS = Enum('API functions', 'MATCHES')
BASE_URL = 'https://api.dc01.gamelockerapp.com/shards/global'

class Client:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_url(self, action):
        if action == ACTIONS.MATCHES:
            return f"{BASE_URL}/matches"
        else:
            raise NotImplementedError()

    def call(self, action):
        headers = {
            'Accept': 'application/vnd.api+json',
            'Accept-Encoding': 'gzip',
            'Authorization': f"Bearer {self.api_key}"
        }
        url = self.get_url(action)

        if action == ACTIONS.MATCHES:
            response = requests.get(url, headers=headers)
        else:
            raise NotImplementedError()

        return response.json()
