# Clash Royale Events System

Real-time monitoring and event callbacks for the Clash Royale API.

## Quick Start

```python
import clashroyale

# Create the events client
client = clashroyale.EventsClient()
client.login_with_token("your_api_token")

# Register an event listener
@client.event
@clashroyale.ClanEvents.member_join()
async def on_member_join(member, clan):
    print(f"{member.name} joined {clan.name}")

# Subscribe to updates
client.add_clan_updates("#CLAN_TAG")

# Start polling
client.run_forever()
```

---

## EventsClient

The `EventsClient` extends the base API client with background polling and event dispatching.

### Initialization

```python
import clashroyale

# Create client
client = clashroyale.EventsClient()

# Login with token
client.login_with_token("your_api_token")

# Configure polling intervals (optional, in seconds)
client.clan_update_interval = 60      # Default: 60 seconds
client.player_update_interval = 60    # Default: 60 seconds
client.war_update_interval = 60       # Default: 60 seconds
```

### Subscription Methods

```python
# Subscribe to clan updates (member changes, clan stat changes)
client.add_clan_updates("#2PP")
client.add_clan_updates(["#2PP", "#ABC123"])

# Subscribe to player updates (trophy changes, card unlocks, etc.)
client.add_player_updates("#PLAYER1")
client.add_player_updates(["#PLAYER1", "#PLAYER2"])

# Subscribe to war updates (river race tracking)
client.add_war_updates("#2PP")  # Uses clan tag
client.add_war_updates(["#2PP", "#ABC123"])

# Remove subscriptions
client.remove_clan_updates("#2PP")
client.remove_player_updates("#PLAYER1")
client.remove_war_updates("#2PP")
```

### Event Registration

```python
# Method 1: Decorator syntax
@client.event
@clashroyale.ClanEvents.member_join()
async def on_member_join(member, clan):
    print(f"{member.name} joined {clan.name}")

# Method 2: add_events() method
async def on_trophy_change(old_player, new_player):
    diff = new_player.trophies - old_player.trophies
    print(f"{new_player.name}: {diff:+d} trophies")

client.add_events(
    clashroyale.PlayerEvents.trophies()(on_trophy_change)
)
```

### Running the Client

```python
# Run forever (blocking)
client.run_forever()

# Or run in an existing async context
import asyncio

async def main():
    await client.start()
    # ... your code ...
    await client.close()

asyncio.run(main())
```

---

## ClanEvents

Events triggered by changes to clan data.

### Predefined Events

#### member_join

Triggered when a new member joins the clan.

```python
@client.event
@clashroyale.ClanEvents.member_join()
async def on_member_join(member, clan):
    """
    Args:
        member: ClanMember - The member who joined
        clan: Clan - The clan they joined
    """
    print(f"{member.name} ({member.tag}) joined {clan.name}")
    print(f"Role: {member.role}")
    print(f"Trophies: {member.trophies}")
```

#### member_leave

Triggered when a member leaves the clan.

```python
@client.event
@clashroyale.ClanEvents.member_leave()
async def on_member_leave(member, clan):
    """
    Args:
        member: ClanMember - The member who left (cached data)
        clan: Clan - The clan they left
    """
    print(f"{member.name} left {clan.name}")
```

### Dynamic Clan Events

Any clan attribute can be monitored by using it as an event name:

```python
# Clan name changed
@client.event
@clashroyale.ClanEvents.name()
async def on_name_change(old_clan, new_clan):
    print(f"Clan renamed: {old_clan.name} -> {new_clan.name}")

# Clan description changed
@client.event
@clashroyale.ClanEvents.description()
async def on_desc_change(old_clan, new_clan):
    print(f"Description updated for {new_clan.name}")

# Clan score changed
@client.event
@clashroyale.ClanEvents.clan_score()
async def on_score_change(old_clan, new_clan):
    diff = new_clan.clan_score - old_clan.clan_score
    print(f"{new_clan.name} score: {diff:+d}")

# Clan war trophies changed
@client.event
@clashroyale.ClanEvents.clan_war_trophies()
async def on_war_trophies_change(old_clan, new_clan):
    print(f"War trophies: {old_clan.clan_war_trophies} -> {new_clan.clan_war_trophies}")

# Clan type changed (open/inviteOnly/closed)
@client.event
@clashroyale.ClanEvents.type()
async def on_type_change(old_clan, new_clan):
    print(f"{new_clan.name} is now {new_clan.type}")

# Required trophies changed
@client.event
@clashroyale.ClanEvents.required_trophies()
async def on_req_change(old_clan, new_clan):
    print(f"Required: {old_clan.required_trophies} -> {new_clan.required_trophies}")

# Weekly donations changed
@client.event
@clashroyale.ClanEvents.donations_per_week()
async def on_donations_change(old_clan, new_clan):
    print(f"Donations this week: {new_clan.donations_per_week}")
```

### Nested Member Events

Monitor changes to individual members within a clan using the `member_` prefix:

```python
# Member trophies changed
@client.event
@clashroyale.ClanEvents.member_trophies()
async def on_member_trophies(old_member, new_member, clan):
    """
    Args:
        old_member: ClanMember - The member's previous state
        new_member: ClanMember - The member's current state
        clan: Clan - The clan they belong to
    """
    diff = new_member.trophies - old_member.trophies
    print(f"{new_member.name} in {clan.name}: {diff:+d} trophies")

# Member role changed (member -> elder -> coLeader -> leader)
@client.event
@clashroyale.ClanEvents.member_role()
async def on_role_change(old_member, new_member, clan):
    print(f"{new_member.name}: {old_member.role} -> {new_member.role}")

# Member donations changed
@client.event
@clashroyale.ClanEvents.member_donations()
async def on_member_donations(old_member, new_member, clan):
    donated = new_member.donations - old_member.donations
    print(f"{new_member.name} donated {donated} cards")

# Member donations received changed
@client.event
@clashroyale.ClanEvents.member_donations_received()
async def on_donations_received(old_member, new_member, clan):
    received = new_member.donations_received - old_member.donations_received
    print(f"{new_member.name} received {received} cards")

# Member arena changed
@client.event
@clashroyale.ClanEvents.member_arena()
async def on_arena_change(old_member, new_member, clan):
    print(f"{new_member.name} reached {new_member.arena.name}")
```

### Available Clan Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | str | Clan name |
| `description` | str | Clan description |
| `type` | str | open, inviteOnly, closed |
| `badge_id` | int | Clan badge ID |
| `clan_score` | int | Total clan trophies |
| `clan_war_trophies` | int | War league trophies |
| `required_trophies` | int | Join requirement |
| `donations_per_week` | int | Weekly donations |
| `member_count` | int | Number of members |

### Available Member Attributes (with `member_` prefix)

| Attribute | Type | Description |
|-----------|------|-------------|
| `member_trophies` | int | Member's trophies |
| `member_role` | str | member, elder, coLeader, leader |
| `member_donations` | int | Cards donated this week |
| `member_donations_received` | int | Cards received this week |
| `member_arena` | Arena | Current arena |
| `member_exp_level` | int | Experience level |
| `member_last_seen` | str | Last activity timestamp |

---

## PlayerEvents

Events triggered by changes to player data.

### Predefined Events

#### card_unlock

Triggered when a player unlocks a new card.

```python
@client.event
@clashroyale.PlayerEvents.card_unlock()
async def on_card_unlock(old_player, new_player, card):
    """
    Args:
        old_player: Player - Previous player state
        new_player: Player - Current player state
        card: PlayerItemLevel - The newly unlocked card
    """
    print(f"{new_player.name} unlocked {card.name}!")
```

#### card_upgrade

Triggered when a player upgrades a card.

```python
@client.event
@clashroyale.PlayerEvents.card_upgrade()
async def on_card_upgrade(old_player, new_player, old_card, new_card):
    """
    Args:
        old_player: Player - Previous player state
        new_player: Player - Current player state
        old_card: PlayerItemLevel - Card before upgrade
        new_card: PlayerItemLevel - Card after upgrade
    """
    print(f"{new_player.name} upgraded {new_card.name}: Lv{old_card.level} -> Lv{new_card.level}")
```

#### clan_join

Triggered when a player joins a clan.

```python
@client.event
@clashroyale.PlayerEvents.clan_join()
async def on_clan_join(old_player, new_player):
    """
    Args:
        old_player: Player - Previous player state
        new_player: Player - Current player state
    """
    print(f"{new_player.name} joined {new_player.clan.name}")
```

#### clan_leave

Triggered when a player leaves a clan.

```python
@client.event
@clashroyale.PlayerEvents.clan_leave()
async def on_clan_leave(old_player, new_player):
    """
    Args:
        old_player: Player - Previous player state
        new_player: Player - Current player state
    """
    print(f"{new_player.name} left {old_player.clan.name}")
```

### Dynamic Player Events

```python
# Trophies changed
@client.event
@clashroyale.PlayerEvents.trophies()
async def on_trophies(old_player, new_player):
    diff = new_player.trophies - old_player.trophies
    print(f"{new_player.name}: {diff:+d} trophies")

# Best trophies (PB) changed
@client.event
@clashroyale.PlayerEvents.best_trophies()
async def on_new_pb(old_player, new_player):
    print(f"{new_player.name} new PB: {new_player.best_trophies}")

# Experience level changed (level up!)
@client.event
@clashroyale.PlayerEvents.exp_level()
async def on_level_up(old_player, new_player):
    print(f"{new_player.name} reached level {new_player.exp_level}!")

# Name changed
@client.event
@clashroyale.PlayerEvents.name()
async def on_name_change(old_player, new_player):
    print(f"{old_player.name} is now {new_player.name}")

# Wins changed
@client.event
@clashroyale.PlayerEvents.wins()
async def on_win(old_player, new_player):
    new_wins = new_player.wins - old_player.wins
    print(f"{new_player.name} won {new_wins} battle(s)")

# Losses changed
@client.event
@clashroyale.PlayerEvents.losses()
async def on_loss(old_player, new_player):
    new_losses = new_player.losses - old_player.losses
    print(f"{new_player.name} lost {new_losses} battle(s)")

# Donations changed
@client.event
@clashroyale.PlayerEvents.donations()
async def on_donate(old_player, new_player):
    donated = new_player.donations - old_player.donations
    print(f"{new_player.name} donated {donated} cards")

# Current favourite card changed
@client.event
@clashroyale.PlayerEvents.current_favourite_card()
async def on_fav_card(old_player, new_player):
    print(f"{new_player.name}'s favorite: {new_player.current_favourite_card.name}")

# Star points changed
@client.event
@clashroyale.PlayerEvents.star_points()
async def on_star_points(old_player, new_player):
    gained = new_player.star_points - old_player.star_points
    print(f"{new_player.name} gained {gained} star points")
```

### Available Player Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | str | Player name |
| `trophies` | int | Current trophies |
| `best_trophies` | int | Personal best trophies |
| `exp_level` | int | Experience level |
| `exp_points` | int | Experience points |
| `wins` | int | Total wins |
| `losses` | int | Total losses |
| `three_crown_wins` | int | Three crown wins |
| `donations` | int | Donations this season |
| `donations_received` | int | Donations received this season |
| `challenge_cards_won` | int | Challenge cards won |
| `challenge_max_wins` | int | Max challenge wins |
| `tournament_cards_won` | int | Tournament cards won |
| `tournament_battle_count` | int | Tournament battles |
| `star_points` | int | Star points |
| `current_favourite_card` | Item | Favorite card |
| `arena` | Arena | Current arena |
| `clan` | PlayerClan | Player's clan (or None) |

---

## WarEvents

Events triggered by river race (Clan War 2) changes.

### Predefined Events

#### new_river_race

Triggered when a new river race week starts.

```python
@client.event
@clashroyale.WarEvents.new_river_race()
async def on_new_war(war):
    """
    Args:
        war: CurrentRiverRace - The new river race
    """
    print(f"New river race week {war.section_index} started!")
    print(f"Clans participating: {len(war.clans)}")
```

#### war_day_start

Triggered when training period ends and war day begins.

```python
@client.event
@clashroyale.WarEvents.war_day_start()
async def on_war_day(war):
    """
    Args:
        war: CurrentRiverRace - The current river race
    """
    print(f"War day has begun! Period: {war.period_type}")
```

#### war_end

Triggered when the river race ends.

```python
@client.event
@clashroyale.WarEvents.war_end()
async def on_war_end(war):
    """
    Args:
        war: CurrentRiverRace - The ended river race
    """
    print("River race has ended!")
    # Find the winner
    winner = max(war.clans, key=lambda c: c.fame)
    print(f"Winner: {winner.name} with {winner.fame} fame")
```

### Dynamic War Events

```python
# War state changed (matchmaking, matched, full, ended)
@client.event
@clashroyale.WarEvents.state()
async def on_state_change(old_war, new_war):
    print(f"War state: {old_war.state} -> {new_war.state}")

# Period type changed (training, war_day, colosseum)
@client.event
@clashroyale.WarEvents.period_type()
async def on_period_change(old_war, new_war):
    print(f"Period: {old_war.period_type} -> {new_war.period_type}")

# Section index changed (new week in season)
@client.event
@clashroyale.WarEvents.section_index()
async def on_section_change(old_war, new_war):
    print(f"Week {old_war.section_index} -> Week {new_war.section_index}")

# Period index changed
@client.event
@clashroyale.WarEvents.period_index()
async def on_period_index(old_war, new_war):
    print(f"Period index: {old_war.period_index} -> {new_war.period_index}")
```

### Available War Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `state` | str | matchmaking, matched, full, ended |
| `period_type` | str | training, war_day, colosseum |
| `section_index` | int | Current week in the season |
| `period_index` | int | Current period |
| `clans` | list | List of RiverRaceClan objects |

---

## ClientEvents

Events triggered by the EventsClient itself, not data changes.

### maintenance_start

Triggered when API maintenance is detected (503 errors).

```python
@client.event
@clashroyale.ClientEvents.maintenance_start()
async def on_maintenance():
    print("Clash Royale API is under maintenance!")
```

### maintenance_completion

Triggered when maintenance ends and API is available again.

```python
@client.event
@clashroyale.ClientEvents.maintenance_completion()
async def on_maintenance_end(time_started):
    """
    Args:
        time_started: datetime - When maintenance began
    """
    from datetime import datetime, timezone
    duration = datetime.now(timezone.utc) - time_started
    print(f"Maintenance ended! Duration: {duration}")
```

### event_error

Triggered when an unhandled error occurs during event processing.

```python
@client.event
@clashroyale.ClientEvents.event_error()
async def on_error(exception):
    """
    Args:
        exception: Exception - The error that occurred
    """
    print(f"Event error: {type(exception).__name__}: {exception}")
```

### Loop Events

Track polling loop activity:

```python
@client.event
@clashroyale.ClientEvents.clan_loop_start()
async def on_clan_loop_start(loop_count):
    print(f"Starting clan update cycle #{loop_count}")

@client.event
@clashroyale.ClientEvents.clan_loop_finish()
async def on_clan_loop_finish(loop_count):
    print(f"Finished clan update cycle #{loop_count}")

@client.event
@clashroyale.ClientEvents.player_loop_start()
async def on_player_loop_start(loop_count):
    print(f"Starting player update cycle #{loop_count}")

@client.event
@clashroyale.ClientEvents.player_loop_finish()
async def on_player_loop_finish(loop_count):
    print(f"Finished player update cycle #{loop_count}")

@client.event
@clashroyale.ClientEvents.war_loop_start()
async def on_war_loop_start(loop_count):
    print(f"Starting war update cycle #{loop_count}")

@client.event
@clashroyale.ClientEvents.war_loop_finish()
async def on_war_loop_finish(loop_count):
    print(f"Finished war update cycle #{loop_count}")
```

---

## Tag Filtering

Filter events to specific tags:

```python
# Only trigger for a specific clan
@client.event
@clashroyale.ClanEvents.member_join(tags="#2PP")
async def on_2pp_join(member, clan):
    print(f"{member.name} joined 2PP!")

# Multiple clans
@client.event
@clashroyale.ClanEvents.member_leave(tags=["#2PP", "#ABC123"])
async def on_leave(member, clan):
    print(f"{member.name} left {clan.name}")

# Specific player
@client.event
@clashroyale.PlayerEvents.trophies(tags="#PLAYER1")
async def on_player1_trophies(old_player, new_player):
    print(f"Player1 trophies: {new_player.trophies}")

# Specific war
@client.event
@clashroyale.WarEvents.war_end(tags="#2PP")
async def on_2pp_war_end(war):
    print("2PP's river race ended!")
```

---

## Dynamic Events Explained

The event system uses Python's `__getattr__` to dynamically create events for any attribute. When you write:

```python
@clashroyale.ClanEvents.clan_score()
```

The system:
1. Checks if `clan_score` is a predefined event method (it's not)
2. Creates a dynamic event that compares `old_clan.clan_score != new_clan.clan_score`
3. If different, triggers your callback with `(old_clan, new_clan)`

This works for any attribute on the model, even ones not explicitly documented.

---

## Utilities

### Tag Correction

Normalize tags to correct format:

```python
from clashroyale import correct_tag

tag = correct_tag("2pp")       # Returns "#2PP"
tag = correct_tag("#2PP")      # Returns "#2PP"
tag = correct_tag("2PPO0")     # Returns "#2PP00" (O -> 0)
```

### Custom Exceptions

```python
from clashroyale import Maintenance, NotFound, InvalidTag, PrivateWarLog

try:
    player = client.get_player("#invalid")
except NotFound:
    print("Player not found!")
except InvalidTag:
    print("Invalid tag format!")
except Maintenance:
    print("API under maintenance!")

try:
    war_log = client.get_clan_river_race_log("#CLAN")
except PrivateWarLog:
    print("This clan's war log is private!")
```

---

## Complete Example

```python
import clashroyale
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Create client
client = clashroyale.EventsClient()
client.login_with_token("your_api_token")

# Configure intervals
client.clan_update_interval = 60
client.player_update_interval = 60
client.war_update_interval = 120

# --- Clan Events ---
@client.event
@clashroyale.ClanEvents.member_join()
async def on_member_join(member, clan):
    print(f"[JOIN] {member.name} joined {clan.name}")

@client.event
@clashroyale.ClanEvents.member_leave()
async def on_member_leave(member, clan):
    print(f"[LEAVE] {member.name} left {clan.name}")

@client.event
@clashroyale.ClanEvents.member_role()
async def on_promotion(old_member, new_member, clan):
    print(f"[ROLE] {new_member.name}: {old_member.role} -> {new_member.role}")

# --- Player Events ---
@client.event
@clashroyale.PlayerEvents.trophies()
async def on_trophies(old_player, new_player):
    diff = new_player.trophies - old_player.trophies
    emoji = "+" if diff > 0 else ""
    print(f"[TROPHIES] {new_player.name}: {emoji}{diff}")

@client.event
@clashroyale.PlayerEvents.card_unlock()
async def on_card_unlock(old_player, new_player, card):
    print(f"[UNLOCK] {new_player.name} unlocked {card.name}!")

@client.event
@clashroyale.PlayerEvents.card_upgrade()
async def on_card_upgrade(old_player, new_player, old_card, new_card):
    print(f"[UPGRADE] {new_player.name}: {new_card.name} Lv{old_card.level} -> Lv{new_card.level}")

@client.event
@clashroyale.PlayerEvents.exp_level()
async def on_level_up(old_player, new_player):
    print(f"[LEVEL UP] {new_player.name} reached level {new_player.exp_level}!")

# --- War Events ---
@client.event
@clashroyale.WarEvents.new_river_race()
async def on_new_war(war):
    print(f"[WAR] New river race week {war.section_index} started!")

@client.event
@clashroyale.WarEvents.war_day_start()
async def on_war_day(war):
    print(f"[WAR] War day has begun!")

@client.event
@clashroyale.WarEvents.war_end()
async def on_war_end(war):
    winner = max(war.clans, key=lambda c: c.fame)
    print(f"[WAR] River race ended! Winner: {winner.name}")

# --- Client Events ---
@client.event
@clashroyale.ClientEvents.maintenance_start()
async def on_maintenance():
    print("[MAINTENANCE] API is under maintenance!")

@client.event
@clashroyale.ClientEvents.maintenance_completion()
async def on_maintenance_end(time_started):
    print(f"[MAINTENANCE] Back online!")

@client.event
@clashroyale.ClientEvents.event_error()
async def on_error(exception):
    print(f"[ERROR] {type(exception).__name__}: {exception}")

# Subscribe to updates
client.add_clan_updates("#2PP")
client.add_player_updates(["#PLAYER1", "#PLAYER2"])
client.add_war_updates("#2PP")

# Run forever
print("Starting Clash Royale event monitoring...")
client.run_forever()
```

---

## Model Reference

### Clan

| Attribute | Type |
|-----------|------|
| `tag` | str |
| `name` | str |
| `description` | str |
| `type` | str |
| `badge_id` | int |
| `clan_score` | int |
| `clan_war_trophies` | int |
| `required_trophies` | int |
| `donations_per_week` | int |
| `member_count` | int |
| `member_list` | list[ClanMember] |
| `location` | Location |

### ClanMember

| Attribute | Type |
|-----------|------|
| `tag` | str |
| `name` | str |
| `role` | str |
| `trophies` | int |
| `arena` | Arena |
| `exp_level` | int |
| `donations` | int |
| `donations_received` | int |
| `last_seen` | str |
| `clan_rank` | int |
| `previous_clan_rank` | int |
| `clan_chest_points` | int |

### Player

| Attribute | Type |
|-----------|------|
| `tag` | str |
| `name` | str |
| `trophies` | int |
| `best_trophies` | int |
| `exp_level` | int |
| `exp_points` | int |
| `wins` | int |
| `losses` | int |
| `three_crown_wins` | int |
| `donations` | int |
| `donations_received` | int |
| `challenge_cards_won` | int |
| `challenge_max_wins` | int |
| `tournament_cards_won` | int |
| `tournament_battle_count` | int |
| `star_points` | int |
| `total_exp_points` | int |
| `cards` | list[PlayerItemLevel] |
| `current_favourite_card` | Item |
| `current_deck` | list[PlayerItemLevel] |
| `achievements` | list[PlayerAchievementProgress] |
| `badges` | list[PlayerAchievementBadge] |
| `arena` | Arena |
| `clan` | PlayerClan |

### CurrentRiverRace

| Attribute | Type |
|-----------|------|
| `state` | str |
| `clan` | RiverRaceClan |
| `clans` | list[RiverRaceClan] |
| `section_index` | int |
| `period_index` | int |
| `period_type` | str |

### RiverRaceClan

| Attribute | Type |
|-----------|------|
| `tag` | str |
| `name` | str |
| `fame` | int |
| `repair_points` | int |
| `finish_time` | str |
| `participants` | list[RiverRaceParticipant] |
| `clan_score` | int |
| `badge_id` | int |
