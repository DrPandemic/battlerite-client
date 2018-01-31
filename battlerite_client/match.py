class Match:
    """
    A Battlerite's match.
    """

    def __init__(self, data) -> None:
        attributes = data['attributes']
        self.id = data['id']
        self.created_at = attributes['createdAt']
        self.duration = attributes['duration']
        self.game_mode = attributes['gameMode']
