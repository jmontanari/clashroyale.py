# Battle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_mode** | [**GameMode**](GameMode.md) |  | [optional] 
**arena** | [**Arena**](Arena.md) |  | [optional] 
**type** | **str** |  | [optional] 
**deck_selection** | **str** |  | [optional] 
**team** | [**List[PlayerBattleData]**](PlayerBattleData.md) |  | [optional] 
**opponent** | [**List[PlayerBattleData]**](PlayerBattleData.md) |  | [optional] 
**challenge_win_count_before** | **int** |  | [optional] 
**boat_battle_side** | **str** |  | [optional] 
**boat_battle_won** | **bool** |  | [optional] 
**new_towers_destroyed** | **int** |  | [optional] 
**prev_towers_destroyed** | **int** |  | [optional] 
**remaining_towers** | **int** |  | [optional] 
**league_number** | **int** |  | [optional] 
**battle_time** | **str** |  | [optional] 
**challenge_id** | **int** |  | [optional] 
**tournament_tag** | **str** |  | [optional] 
**challenge_title** | **str** |  | [optional] 
**is_ladder_tournament** | **bool** |  | [optional] 
**is_hosted_match** | **bool** |  | [optional] 

## Example

```python
from clashroyale.models.battle import Battle

# TODO update the JSON string below
json = "{}"
# create an instance of Battle from a JSON string
battle_instance = Battle.from_json(json)
# print the JSON string representation of the object
print(Battle.to_json())

# convert the object into a dict
battle_dict = battle_instance.to_dict()
# create an instance of Battle from a dict
battle_from_dict = Battle.from_dict(battle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


