from typing import Dict
from .helpers import find_node
from .round import Round
from .roster import Roster

class Match:
    """
    A Battlerite's match.
    """

    def __init__(self, data: Dict, response: Dict) -> None:
        attributes = data.get('attributes', {})
        relationships = data.get('relationships', {})
        tags = attributes.get('tags')
        links = data.get('links', {})
        stats = attributes.get('stats', {})

        self.id = data.get('id')
        self.created_at = attributes.get('createdAt')
        self.duration = attributes.get('duration')
        self.game_mode = attributes.get('gameMode')
        self.patch_version = attributes.get('patchVersion')
        self.shard_id = attributes.get('shardId')
        self.map_id = stats.get('mapID')
        self.type = stats.get('type')
        self.tags = attributes.get('tags')
        self.title_id = attributes.get('titleId')
        self.link_schema = links.get('schema')
        self.link = links.get('self')
        if type(tags) is dict:
            self.ranking_type = tags.get('rankingType')
            self.server_type = tags.get('serverType')
        else:
            self.ranking_type = None
            self.server_type = None

        rounds = relationships.get('rounds', {}).get('data', [])
        rosters = relationships.get('rosters', {}).get('data', [])
        self.rounds = [Round(find_node(response, r['id'])) for r in rounds]
        self.rosters = [Roster(find_node(response, r['id']), response)
                        for r in rosters]
        self.spectators = relationships.get('spectators', [])
        self.links = [link['self'] for link in relationships.get('links', [])]
