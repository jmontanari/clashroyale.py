# PlayerBattleRound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cards** | [**List[PlayerItemLevel]**](PlayerItemLevel.md) |  | [optional] 
**elixir_leaked** | **object** |  | [optional] 
**crowns** | **int** |  | [optional] 
**king_tower_hit_points** | **int** |  | [optional] 
**princess_towers_hit_points** | **List[int]** |  | [optional] 

## Example

```python
from clashroyale.models.player_battle_round import PlayerBattleRound

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerBattleRound from a JSON string
player_battle_round_instance = PlayerBattleRound.from_json(json)
# print the JSON string representation of the object
print(PlayerBattleRound.to_json())

# convert the object into a dict
player_battle_round_dict = player_battle_round_instance.to_dict()
# create an instance of PlayerBattleRound from a dict
player_battle_round_from_dict = PlayerBattleRound.from_dict(player_battle_round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


