# coding: utf-8

"""
    Clash Royale API - Events

    Event system for the Clash Royale API, providing decorator-based event
    registration and change detection for players, clans, and wars.

    This module provides:
    - Event: Core event wrapper class
    - _ValidateEvent: Dynamic event creation helper
    - ClanEvents: Predefined clan events (member_join, member_leave, etc.)
    - PlayerEvents: Predefined player events (card_unlock, clan_join, etc.)
    - WarEvents: War/River Race events (new_river_race, etc.)
    - ClientEvents: Client/misc events (maintenance, errors, etc.)

    Example usage:
        import clashroyale

        @clashroyale.ClanEvents.member_join()
        async def on_member_join(member, clan):
            print(f"{member.name} joined {clan.name}")

        @clashroyale.WarEvents.new_river_race()
        async def on_new_war(war):
            print(f"New river race started!")
"""

import asyncio
import logging
from collections.abc import Iterable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from clashroyale.models.clan import Clan
    from clashroyale.models.player import Player
    from clashroyale.models.current_river_race import CurrentRiverRace

LOG = logging.getLogger(__name__)


class Event:
    """
    Object that is created for an event. This contains runner functions,
    tags and type.

    Attributes
    ----------
    runner : coroutine
        The async function that checks conditions and executes the callback.
    callback : coroutine
        The user's event listener function.
    tags : tuple
        Filter tags (e.g., specific clan/player tags).
    type : str
        Event category: "clan", "player", "war", or "client".
    """

    __slots__ = ("runner", "callback", "tags", "type")

    def __init__(self, runner, callback, tags, type_):
        self.runner = runner
        self.callback = callback
        self.tags = tags
        self.type = type_

    def __call__(self, cached, current):
        return self.runner(cached, current, self.callback)

    def __eq__(self, other):
        return (
            isinstance(self, other.__class__)
            and self.runner == other.runner
            and self.callback == other.callback
        )

    @classmethod
    def from_decorator(cls, func, runner):
        """Helper classmethod to create an event from a decorated function."""
        return cls(runner, func, func.event_tags, func.event_type)


class _ValidateEvent:
    """Helper class to validate and register a function as an event.

    This class enables dynamic event creation through attribute access,
    allowing events like `@ClanEvents.clan_score()` to work automatically
    for any model attribute.
    """

    def __init__(self, cls):
        self.cls = cls

    def __getattr__(self, item: str):
        try:
            return getattr(self.cls, item)
        except AttributeError:
            pass

        if self.cls.event_type == "client":
            return self.cls.__getattr__(self.cls, item)

        # Handle member_x events for nested clan member attributes
        if "member_" in item and item not in ("member_list", "member_count"):
            item = item.replace("member_", "")
            nested = True
        else:
            nested = False

        return self._create_event(item.replace("_change", ""), nested)

    def _create_event(self, item, nested=False):
        def pred(cached, live) -> bool:
            return getattr(cached, item, None) != getattr(live, item, None)

        def actual(tags=None, custom_class=None, retry_interval=None):
            try:
                # Don't type check if it's nested
                custom_class and not nested and getattr(custom_class, item)
            except AttributeError:
                raise RuntimeError(f"custom_class does not have expected attribute {item}")

            def decorator(func):
                if nested:
                    wrap = _ValidateEvent.wrap_clan_member_pred
                else:
                    wrap = _ValidateEvent.wrap_pred
                return _ValidateEvent.register_event(
                    func, wrap(pred), tags, custom_class, retry_interval, self.cls.event_type, item
                )

            return decorator

        return actual

    @staticmethod
    def shortcut_register(wrapped, tags, custom_class, retry_interval, event_type):
        """Fast route of registering an event for custom events that are manually defined."""

        def decorator(func):
            return _ValidateEvent.register_event(func, wrapped, tags, custom_class, retry_interval, event_type)

        return decorator

    @staticmethod
    def wrap_pred(pred):
        """Wraps a predicate in a coroutine that awaits the callback if the predicate is True."""

        async def wrapped(cached, live, callback):
            if pred(cached, live):
                await callback(cached, live)

        return wrapped

    @staticmethod
    def wrap_clan_member_pred(pred):
        """Wraps a predicate for a clan member (nested) attribute, and calls the callback."""

        async def wrapped(cached_clan: "Clan", clan: "Clan", callback):
            for member in clan.member_list or []:
                cached_member = next(
                    (m for m in (cached_clan.member_list or []) if m.tag == member.tag),
                    None
                )
                if cached_member is not None and pred(cached_member, member):
                    await callback(cached_member, member, clan)

        return wrapped

    @staticmethod
    def register_event(func, runner, tags=None, cls=None, retry_interval=None, event_type="", event_name=""):
        """Validates the types of all arguments and adds these as attributes to the function."""
        if getattr(func, "is_event_listener", False) and func.event_type != event_type:
            raise RuntimeError("maximum of one event type per callback function.")

        if not asyncio.iscoroutinefunction(func):
            raise TypeError("callback function must be of type coroutine.")

        if not tags:
            tags = ()
        elif isinstance(tags, str):
            tags = (tags,)
        elif isinstance(tags, Iterable):
            tags = tuple(tags)
        else:
            raise TypeError(f"tags must be of type str, or iterable not {tags!r}")

        if retry_interval is not None and not isinstance(retry_interval, int):
            raise TypeError(f"retry_interval must be of type int not {retry_interval!r}")

        if not asyncio.iscoroutinefunction(runner):
            raise TypeError("runner function must be of type coroutine")

        func.event_type = event_type
        func.event_tags = tags
        func.is_event_listener = True
        func.event_cls = cls
        func.event_retry_interval = retry_interval
        func.event_name = event_name

        try:
            func.event_runners.append(runner)
        except AttributeError:
            func.event_runners = [runner]

        return func


@_ValidateEvent
class ClanEvents:
    """Predefined clan events, or create your own with dynamic attribute access.

    Predefined Events
    -----------------
    member_join : Triggered when a member joins the clan
        Callback signature: async def callback(member: ClanMember, clan: Clan)

    member_leave : Triggered when a member leaves the clan
        Callback signature: async def callback(member: ClanMember, clan: Clan)

    Dynamic Events (via attribute access)
    -------------------------------------
    Any clan attribute can be monitored by using it as an event name:
    - name : Clan name changed
    - description : Clan description changed
    - clan_score : Clan score changed
    - clan_war_trophies : Clan war trophies changed
    - type : Clan type changed (open/inviteOnly/closed)
    - required_trophies : Required trophies changed
    - donations_per_week : Weekly donations changed

    Nested member events (prefix with member_):
    - member_trophies : Member trophies changed
    - member_role : Member role changed
    - member_donations : Member donations changed

    Example
    -------
    @clashroyale.ClanEvents.member_join()
    async def on_member_join(member, clan):
        print(f"{member.name} joined {clan.name}")

    @clashroyale.ClanEvents.clan_score()
    async def on_clan_score_change(old_clan, new_clan):
        print(f"Clan score: {old_clan.clan_score} -> {new_clan.clan_score}")

    @clashroyale.ClanEvents.member_role()
    async def on_member_role_change(old_member, new_member, clan):
        print(f"{new_member.name} role: {old_member.role} -> {new_member.role}")
    """

    event_type = "clan"

    @classmethod
    def member_join(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a member has joined the clan.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific clan tags.
        custom_class : class, optional
            Custom Clan class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(member: ClanMember, clan: Clan)
        """

        async def wrapped(cached_clan, clan, callback):
            current_tags = set(n.tag for n in (cached_clan.member_list or []))
            if not current_tags:
                return
            members_joined = (n for n in (clan.member_list or []) if n.tag not in current_tags)
            for member in members_joined:
                await callback(member, clan)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, ClanEvents.event_type)

    @classmethod
    def member_leave(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a member has left the clan.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific clan tags.
        custom_class : class, optional
            Custom Clan class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(member: ClanMember, clan: Clan)
        """

        async def wrapped(cached_clan, clan, callback):
            current_tags = set(n.tag for n in (clan.member_list or []))
            if not current_tags:
                return
            members_left = (n for n in (cached_clan.member_list or []) if n.tag not in current_tags)
            for member in members_left:
                await callback(member, clan)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, ClanEvents.event_type)


@_ValidateEvent
class PlayerEvents:
    """Class that defines all valid player events.

    Predefined Events
    -----------------
    card_unlock : Triggered when a player unlocks a new card
        Callback signature: async def callback(old_player, new_player, card)

    card_upgrade : Triggered when a player upgrades a card
        Callback signature: async def callback(old_player, new_player, old_card, new_card)

    clan_join : Triggered when a player joins a clan
        Callback signature: async def callback(old_player, new_player)

    clan_leave : Triggered when a player leaves a clan
        Callback signature: async def callback(old_player, new_player)

    Dynamic Events (via attribute access)
    -------------------------------------
    Any player attribute can be monitored:
    - trophies : Player trophies changed
    - best_trophies : Best trophies changed
    - exp_level : Experience level changed
    - exp_points : Experience points changed
    - name : Player name changed
    - wins : Wins changed
    - losses : Losses changed
    - donations : Donations changed
    - donations_received : Donations received changed

    Example
    -------
    @clashroyale.PlayerEvents.trophies()
    async def on_trophy_change(old_player, new_player):
        diff = new_player.trophies - old_player.trophies
        print(f"{new_player.name}: {diff:+d} trophies")

    @clashroyale.PlayerEvents.card_unlock()
    async def on_card_unlock(old_player, new_player, card):
        print(f"{new_player.name} unlocked {card.name}!")
    """

    event_type = "player"

    @classmethod
    def card_unlock(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has unlocked a new card.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player, card: PlayerItemLevel)
        """

        async def wrapped(cached_player, player, callback):
            cached_ids = set(c.id for c in (cached_player.cards or []))
            new_cards = (c for c in (player.cards or []) if c.id not in cached_ids)
            for card in new_cards:
                await callback(cached_player, player, card)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)

    @classmethod
    def card_upgrade(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has upgraded a card.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player, old_card: PlayerItemLevel, new_card: PlayerItemLevel)
        """

        async def wrapped(cached_player, player, callback):
            cached_cards = {c.id: c for c in (cached_player.cards or [])}
            for card in player.cards or []:
                cached_card = cached_cards.get(card.id)
                if cached_card and card.level != cached_card.level:
                    await callback(cached_player, player, cached_card, card)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)

    @classmethod
    def clan_join(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has joined a clan.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player)
        """

        async def wrapped(cached_player, player, callback):
            if cached_player.clan is None and player.clan is not None:
                await callback(cached_player, player)
            elif (
                cached_player.clan is not None
                and player.clan is not None
                and cached_player.clan.tag != player.clan.tag
            ):
                await callback(cached_player, player)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)

    @classmethod
    def clan_leave(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has left a clan.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player)
        """

        async def wrapped(cached_player, player, callback):
            if cached_player.clan is not None and player.clan is None:
                await callback(cached_player, player)
            elif (
                cached_player.clan is not None
                and player.clan is not None
                and cached_player.clan.tag != player.clan.tag
            ):
                await callback(cached_player, player)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)


@_ValidateEvent
class WarEvents:
    """Class that defines all valid war (river race) events.

    Predefined Events
    -----------------
    new_river_race : Triggered when a new river race week starts
        Callback signature: async def callback(war: CurrentRiverRace)

    Dynamic Events (via attribute access)
    -------------------------------------
    Any war attribute can be monitored:
    - state : War state changed (matchmaking, matched, full, ended)
    - period_type : Period type changed (training, war_day, colosseum)
    - section_index : Section index changed (new war week)
    - period_index : Period index changed

    Example
    -------
    @clashroyale.WarEvents.new_river_race()
    async def on_new_war(war):
        print(f"New river race week {war.section_index} started!")

    @clashroyale.WarEvents.state()
    async def on_war_state_change(old_war, new_war):
        print(f"War state changed: {old_war.state} -> {new_war.state}")
    """

    event_type = "war"

    @classmethod
    def new_river_race(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a new river race week starts.

        This is triggered when the section_index changes, indicating
        a new war week has begun.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific clan tags.
        custom_class : class, optional
            Custom CurrentRiverRace class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(war: CurrentRiverRace)
        """

        async def wrapped(cached_war: "CurrentRiverRace", war: "CurrentRiverRace", callback):
            # Check if section_index changed (new war week)
            if (
                cached_war.section_index is not None
                and war.section_index is not None
                and cached_war.section_index != war.section_index
            ):
                await callback(war)
            elif war.section_index is not None and cached_war.section_index is None:
                # First time seeing this war
                await callback(war)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, WarEvents.event_type)

    @classmethod
    def war_day_start(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when war day starts (training period ends).

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific clan tags.
        custom_class : class, optional
            Custom CurrentRiverRace class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(war: CurrentRiverRace)
        """

        async def wrapped(cached_war: "CurrentRiverRace", war: "CurrentRiverRace", callback):
            if (
                cached_war.period_type == "training"
                and war.period_type in ("war_day", "colosseum")
            ):
                await callback(war)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, WarEvents.event_type)

    @classmethod
    def war_end(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when the war/river race ends.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific clan tags.
        custom_class : class, optional
            Custom CurrentRiverRace class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(war: CurrentRiverRace)
        """

        async def wrapped(cached_war: "CurrentRiverRace", war: "CurrentRiverRace", callback):
            if cached_war.state != "ended" and war.state == "ended":
                await callback(war)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, WarEvents.event_type)


@_ValidateEvent
class ClientEvents:
    """Class that defines all valid client/misc events.

    These events are triggered by the EventsClient itself, not by changes
    in player, clan, or war data.

    Available Events
    ----------------
    maintenance_start : Triggered when API maintenance is detected
        Callback signature: async def callback()

    maintenance_completion : Triggered when maintenance ends
        Callback signature: async def callback(time_started: datetime)

    event_error : Triggered when an unhandled error occurs in event processing
        Callback signature: async def callback(exception: Exception)

    clan_loop_start : Triggered at the start of each clan update cycle
        Callback signature: async def callback(loop_count: int)

    clan_loop_finish : Triggered at the end of each clan update cycle
        Callback signature: async def callback(loop_count: int)

    player_loop_start : Triggered at the start of each player update cycle
        Callback signature: async def callback(loop_count: int)

    player_loop_finish : Triggered at the end of each player update cycle
        Callback signature: async def callback(loop_count: int)

    war_loop_start : Triggered at the start of each war update cycle
        Callback signature: async def callback(loop_count: int)

    war_loop_finish : Triggered at the end of each war update cycle
        Callback signature: async def callback(loop_count: int)

    Example
    -------
    @clashroyale.ClientEvents.maintenance_start()
    async def on_maintenance():
        print("API is under maintenance!")

    @clashroyale.ClientEvents.event_error()
    async def on_error(exception):
        print(f"Error occurred: {exception}")
    """

    event_type = "client"

    def __getattr__(self, item):
        def wrapped():
            def deco(function):
                function.is_client_event = True
                function.event_name = item
                return function

            return deco

        return wrapped
