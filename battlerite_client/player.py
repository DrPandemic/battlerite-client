from typing import Dict
from .helpers import find_node
from .round import Round

class Player:
    """
    A Battlerite Player.
    """

    def __init__(self, data: Dict) -> None:

        attributes = data.get('attributes')
        links = data.get('links', {})

        self.id = data.get('id')
        self.name = attributes.get('name')
        self.patch_version = attributes.get('patchVersion')
        self.shard_id = attributes.get('shardId')
        self.stats = attributes.get('stats')
        self.title_id = attributes.get('titleId')
        self.link_schema = links.get('schema')
        self.link = links.get('self')
