from typing import Dict

class Round:
    """
    A Battlerite's round.
    """

    def __init__(self, data: Dict) -> None:
        attributes = data['attributes']
        self.id = data['id']
        self.duration = attributes['duration']
        self.ordinal = attributes['ordinal']
        self.winning_team = attributes['stats']['winningTeam']
