# Player


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan** | [**PlayerClan**](PlayerClan.md) |  | [optional] 
**legacy_trophy_road_high_score** | **int** |  | [optional] 
**current_deck** | [**List[PlayerItemLevel]**](PlayerItemLevel.md) |  | [optional] 
**current_deck_support_cards** | [**List[PlayerItemLevel]**](PlayerItemLevel.md) |  | [optional] 
**arena** | [**Arena**](Arena.md) |  | [optional] 
**role** | **str** |  | [optional] 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**total_donations** | **int** |  | [optional] 
**league_statistics** | [**PlayerLeagueStatistics**](PlayerLeagueStatistics.md) |  | [optional] 
**cards** | [**List[PlayerItemLevel]**](PlayerItemLevel.md) |  | [optional] 
**support_cards** | [**List[PlayerItemLevel]**](PlayerItemLevel.md) |  | [optional] 
**current_favourite_card** | [**Item**](Item.md) |  | [optional] 
**badges** | [**List[PlayerAchievementBadge]**](PlayerAchievementBadge.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**exp_level** | **int** |  | [optional] 
**trophies** | **int** |  | [optional] 
**best_trophies** | **int** |  | [optional] 
**donations** | **int** |  | [optional] 
**donations_received** | **int** |  | [optional] 
**achievements** | [**List[PlayerAchievementProgress]**](PlayerAchievementProgress.md) |  | [optional] 
**battle_count** | **int** |  | [optional] 
**three_crown_wins** | **int** |  | [optional] 
**challenge_cards_won** | **int** |  | [optional] 
**challenge_max_wins** | **int** |  | [optional] 
**tournament_cards_won** | **int** |  | [optional] 
**tournament_battle_count** | **int** |  | [optional] 
**war_day_wins** | **int** |  | [optional] 
**clan_cards_collected** | **int** |  | [optional] 
**star_points** | **int** |  | [optional] 
**exp_points** | **int** |  | [optional] 
**total_exp_points** | **int** |  | [optional] 
**current_path_of_legend_season_result** | [**PathOfLegendSeasonResult**](PathOfLegendSeasonResult.md) |  | [optional] 
**last_path_of_legend_season_result** | [**PathOfLegendSeasonResult**](PathOfLegendSeasonResult.md) |  | [optional] 
**best_path_of_legend_season_result** | [**PathOfLegendSeasonResult**](PathOfLegendSeasonResult.md) |  | [optional] 
**progress** | **object** |  | [optional] 

## Example

```python
from clashroyale.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print(Player.to_json())

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_from_dict = Player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


