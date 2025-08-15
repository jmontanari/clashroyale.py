from typing import List, Annotated

from pydantic import StrictStr, Field

from clashroyale import ApiClient, CardsApi, Items, ChallengesApi, ChallengeChain, ClansApi, Clan, ClanMember, \
    ClanWarLogEntry, GlobaltournamentsApi, LeaderboardsApi, LocationsApi, PlayersApi, TournamentsApi, Configuration, \
    Player


class ClashRoyaleClient:
    def __init__(self):
        self.configuration = Configuration()
        self.configuration.api_key_prefix['JWT'] = 'Bearer'
        self.client = None

    def login(self, username: str, password: str):
        """Retrieves all keys and creates an HTTP connection ready for use.

        Parameters
        ----------
        username : str
            Your password email from https://developer.clashroyale.com
            This is used when updating keys automatically if your IP changes

        password : str
            Your password login from https://developer.clashroyale.com
            This is used when updating keys automatically if your IP changes
        """
        self.configuration.username = username
        self.configuration.password = password

        self.client = ApiClient(self.configuration)
        self.client.init_keys()

    def login_with_token(self, token: str) -> None:
        """Creates an HTTP connection ready for use with the tokens you provide.

        Parameters
        ----------
        token: str
            Token as found from https://developer.clashroyale.com under "My account" -> <your key> -> "token".
        """
        self.configuration.api_key['JWT'] = token
        self.client = ApiClient(self.configuration)

    def get_cards_api(self) -> CardsApi:
        return CardsApi(self.client)

    def get_challenges_api(self)->ChallengesApi:
        return ChallengesApi(self.client)

    def get_clans_api(self)->ClansApi:
        return ClansApi(self.client)

    def get_global_tournaments_api(self) ->GlobaltournamentsApi:
        return GlobaltournamentsApi(self.client)

    def get_leaderboards_api(self) ->LeaderboardsApi:
        return LeaderboardsApi(self.client)

    def get_locations_api(self) ->LocationsApi:
        return LocationsApi(self.client)

    def get_players_api(self) ->PlayersApi:
        return PlayersApi(self.client)

    def get_player(self, player_tag: str) -> Player:
        response = PlayersApi(self.client).get_player(self.__to_annotated_str(player_tag))
        return response

    def get_tournaments_api(self) ->TournamentsApi:
        return TournamentsApi(self.client)

    def __to_annotated_str(self, value: str) -> Annotated[StrictStr, Field(description="Identifier")]:
        return Annotated[StrictStr, Field(description="Identifier of the brawler.")](value)
