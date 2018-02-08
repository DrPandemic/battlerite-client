from typing import Dict
from .participant import Participant
from .helpers import find_node

class Roster:
    """
    A Battlerite's roster.
    """

    def __init__(self, data: Dict, response: Dict) -> None:
        attributes = data.get('attributes', {})
        self.id = data.get('id')
        self.shard_id = attributes.get('shardId')
        self.score = attributes.get('stats', {}).get('score')
        self.won = attributes.get('won') == 'true'

        participants = data.get('relationships', {}).get('participants', {}).get('data', [])
        self.participants = [Participant(find_node(response, p['id']), response)
                             for p in participants]
