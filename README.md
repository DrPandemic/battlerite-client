# Battlerite Client
A python API client for
[Battlerite's API](https://battlerite-docs.readthedocs.io).

# Disclaimers
This project is not complete. We are not planning to parse everything right now.
For example, the telemetry API call and the assets relationships are not
managed. We are implementing what we need for our other
[project Battlerates](https://github.com/DrPandemic/battlerates). If you need
more, feel free to open a PR.

# Usage
The data structure we expose is really similar to the one from the
[official API](https://battlerite-docs.readthedocs.io) but a little bit more
flattened. We often merge many objects into a single one.

This is an example to get a player's team's division.
```python
from battlerite_client.client import Client, ACTIONS

client = Client('my-secret-api-key')
# client.teams(season: int, player_id: int) -> [Team]
response = client.teams(6, 2000)
if response.success:
    print([team.division for team in response.parse()])
else:
    print('Your query failed.')
    print(response.raw)
```

# API
## Client
It's the class used to interact with the API.

### __init__
`Client(api_key: str)`

Creates a client object for with an API key. This key will be used for every
API call.

### matches
`client.matches(params: Dict = {}) -> Response`

Returns a list of matches. The params object is directly passed to the query.
From the [official API documentation](https://battlerite-docs.readthedocs.io/en/master/matches/matches.html).

Parameter               | Default    | Description
----------------------- | ---------- | ------------------------------------------------------------------------------------------------
page[offset]            | 0          | Allows paging over results
page[limit]             | 5          | The default (and current maximum) is 5. Values less than 5 and greater than 1 are supported.
sort                    | createdAt  | By default, Matches are sorted by creation time ascending.
filter[createdAt-start] | Now-28days | Must occur before end time. Format is iso8601 Usage: filter[createdAt-start]=2017-01-01T08:25:30Z
filter[createdAt-end]   | Now        | Queries search the last 3 hrs. Format is iso8601 i.e.filter[createdAt-end]=2017-01-01T13:25:30Z
filter[playerIds]       | none       | Filters by player Id. Usage:filter[playerIds]=playerId,playerId,…
filter[patchVersion]    | none       | Filter by Battlerite patch version. Usage: filter[patchVersion]=2.10,2.11,…
filter[serverType]      | none       | Filter by match server type. Usage: filter[serverType]=QUICK2V2,QUICK3v3,…
filter[rankingType]     | none       | Filter by match ranking type. Usage: filter[rankingType]=RANKED

```python
matches = client.matches({ 'page[offset]': 1 })
```

### teams
`client.teams(season: int, player_ids: [int]) -> Response`

Returns a list of teams for given players during a season.

## Response
It represents a response from the API.

### attributes
- `response.raw -> Requests.response` The raw response from the Requests
library.
- `response.action -> ACTIONS` The action used to received this response.
- `response.success -> bool` If the request was successful.
- `response.rate_limit_limit -> int` The limit of request per minute.
- `response.rate_limit_remaining -> int` The number of remaining request.
- `response.rate_limit_reset -> int` The number of nanosecond before the next
reset.

### parse
`response.parse() -> ?Object`

Returns `None` if the query was not successful.

Returns an object according to the action. For example, if the `matches` was
called on `Client` this parse will return a list of `Match`.

## Match
### attributes
- `match.id -> str`
- `match.created_at -> str`
- `match.duration -> int`
- `match.game_mode -> str`
- `match.patch_version -> str`
- `match.shard_id -> str`
- `match.map_id -> str`
- `match.type -> str`
- `match.tags -> str`
- `match.title_id -> str`
- `match.link_schema -> str`
- `match.link -> str`
- `match.ranking_type -> str`
- `match.server_type -> str`
- `match.rounds -> [Round]`
- `match.rosters -> [Roster]`
- `match.spectators -> [str]`
- `match.links -> [str]`

## Round
### attributes
- `match.id -> str`
- `match.duration -> int`
- `match.ordinal -> int`
- `match.winning_team -> int`

## Roster
### attributes
- `match.id -> str`
- `match.shard_id -> str`
- `match.score -> int`
- `match.won -> bool`
- `match.participants -> [Participant]`

## Participant
### attributes
- `match.id -> str`
- `match.actor -> str`
- `match.shard_id -> str`
- `match.ability_uses -> int`
- `match.attachment -> int`
- `match.damage_done -> int`
- `match.damage_received -> int`
- `match.deaths -> int`
- `match.disables_done -> int`
- `match.disables_received -> int`
- `match.emote -> int`
- `match.energy_gained -> int`
- `match.energy_used -> int`
- `match.healing_done -> int`
- `match.healing_received -> int`
- `match.kills -> int`
- `match.mount -> int`
- `match.outfit -> int`
- `match.score -> int`
- `match.side -> int`
- `match.time_alive -> int`

## Team
### attributes
- `match.id -> str`
- `match.shard_id -> str`
- `match.avatar -> int`
- `match.division -> int`
- `match.division_rating -> int`
- `match.league -> int`
- `match.losses -> int`
- `match.members -> [int]`
- `match.placement_gamesLeft -> int`
- `match.top_division -> int`
- `match.top_divisionRating -> int`
- `match.top_league -> int`
- `match.wins -> int`
- `match.title_id -> str`
