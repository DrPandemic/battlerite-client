from typing import Dict
from .helpers import find_node
from .round import Round

class Match:
    """
    A Battlerite's match.
    """

    def __init__(self, data: Dict, response: Dict) -> None:
        attributes = data['attributes']
        relationships = data['relationships']
        tags = data.get('tags', {})
        links = data.get('links', {})
        stats = data.get('stats', {})

        self.id = data['id']
        self.created_at = attributes['createdAt']
        self.duration = attributes['duration']
        self.game_mode = attributes['gameMode']
        self.patch_version = attributes['patchVersion']
        self.shard_id = attributes['shardId']
        self.map_id = stats.get('mapID')
        self.type = stats.get('type')
        self.tags = attributes['tags']
        self.title_id = attributes['titleId']
        self.link_schema = links.get('schema')
        self.link = links.get('self')
        self.ranking_type = tags.get('rankingType')
        self.server_type = tags.get('serverType')

        self.rounds = [Round(find_node(response, r['id'])) for r in relationships['rounds']['data']]
