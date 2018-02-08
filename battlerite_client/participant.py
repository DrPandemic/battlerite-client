from typing import Dict
from .helpers import find_node
from .player import Player

class Participant:
    """
    A Battlerite's participant.
    """

    def __init__(self, data: Dict, response: Dict) -> None:
        attributes = data.get('attributes', {})
        stats = attributes.get('stats', {})
        relationships = data.get('relationships', {})

        self.id = data.get('id')
        self.actor = attributes.get('actor')
        self.shard_id = attributes.get('shardId')
        self.ability_uses = stats.get('abilityUses')
        self.attachment = stats.get('attachment')
        self.damage_done = stats.get('damageDone')
        self.damage_received = stats.get('damageReceived')
        self.deaths = stats.get('deaths')
        self.disables_done = stats.get('disablesDone')
        self.disables_received = stats.get('disablesReceived')
        self.emote = stats.get('emote')
        self.energy_gained = stats.get('energyGained')
        self.energy_used = stats.get('energyUsed')
        self.healing_done = stats.get('healingDone')
        self.healing_received = stats.get('healingReceived')
        self.kills = stats.get('kills')
        self.mount = stats.get('mount')
        self.outfit = stats.get('outfit')
        self.score = stats.get('score')
        self.side = stats.get('side')
        self.time_alive = stats.get('timeAlive')

        player = relationships.get('player', {}).get('data', [])
        self.player = Player(find_node(response, player['id']))

