from typing import Dict
from .helpers import find_node
from .round import Round

class Player:
    """
    A Battlerite Player.
    """

    def __init__(self, data: Dict, response: Dict) -> None:
        attributes = data.get('attributes')
        links = data.get('links', {})

        self.id = data.get('id')
        self.name = attributes.get('name')
        self.patchVersion = attributes.get('patchVersion')
        self.shardId = attributes.get('shardId')
        self.stats = attributes.get('stats')
        self.titleId = attributes.get('titleId')
        self.link_schema = links.get('schema')
        self.link = links.get('self')
