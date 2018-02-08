from typing import Dict

class Team:
    """
    A Battlerite's team.
    """

    def __init__(self, data: Dict, response: Dict) -> None:
        attributes = data.get('attributes', {})
        stats = attributes.get('stats', {})
        self.id = data.get('id')
        self.shard_id = data.get('shardId')
        self.avatar = stats.get('avatar')
        self.division = stats.get('division')
        self.division_rating = stats.get('divisionRating')
        self.league = stats.get('league')
        self.losses = stats.get('losses')
        self.members = stats.get('members', [])
        self.placement_gamesLeft = stats.get('placementGamesLeft')
        self.top_division = stats.get('topDivision')
        self.top_divisionRating = stats.get('topDivisionRating')
        self.top_league = stats.get('topLeague')
        self.wins = stats.get('wins')
        self.title_id = data.get('titleId')