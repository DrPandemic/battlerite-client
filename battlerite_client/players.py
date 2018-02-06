from typing import Dict
from .helpers import find_node
from .round import Round

class Player:
    """
    A Battlerite Player.
    """
    
    def __init__(self, data: Dict, response: Dict) -> None:
        attributes = data['attributes']
        relationships = data['relationships']
        links = data.get('links', {})
        
        self.id = data['id']
        self.name = attributes['name']
        self.patchVersion = attributes['patchVersion']
        self.shardId = attributes['shardId']
        self.stats = attributes['stats']
        self.titleId = attributes['titleId']
        self.link_schema = links.get('schema')
        self.link = links.get('self')
        