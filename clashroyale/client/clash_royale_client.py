from typing import List, Annotated

from pydantic import StrictStr, Field

# Import directly from submodules to avoid circular imports
# (events_client imports this before __init__.py finishes loading)
from clashroyale.api_client import ApiClient
from clashroyale.configuration import Configuration
from clashroyale.api.cards_api import CardsApi
from clashroyale.api.challenges_api import ChallengesApi
from clashroyale.api.clans_api import ClansApi
from clashroyale.api.globaltournaments_api import GlobaltournamentsApi
from clashroyale.api.leaderboards_api import LeaderboardsApi
from clashroyale.api.locations_api import LocationsApi
from clashroyale.api.players_api import PlayersApi
from clashroyale.api.tournaments_api import TournamentsApi
from clashroyale.models.items import Items
from clashroyale.models.challenge_chain import ChallengeChain
from clashroyale.models.clan import Clan
from clashroyale.models.clan_member import ClanMember
from clashroyale.models.clan_war_log_entry import ClanWarLogEntry
from clashroyale.models.player import Player


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
        return GlobaltournamentsApi(self.client).get_global_tournaments

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
