# PlayerBattleData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan** | [**PlayerClan**](PlayerClan.md) |  | [optional] 
**cards** | [**List[PlayerItemLevel]**](PlayerItemLevel.md) |  | [optional] 
**support_cards** | [**List[PlayerItemLevel]**](PlayerItemLevel.md) |  | [optional] 
**rounds** | [**List[PlayerBattleRound]**](PlayerBattleRound.md) |  | [optional] 
**crowns** | **int** |  | [optional] 
**princess_towers_hit_points** | **List[int]** |  | [optional] 
**elixir_leaked** | **object** |  | [optional] 
**global_rank** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**starting_trophies** | **int** |  | [optional] 
**trophy_change** | **int** |  | [optional] 
**king_tower_hit_points** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.player_battle_data import PlayerBattleData

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerBattleData from a JSON string
player_battle_data_instance = PlayerBattleData.from_json(json)
# print the JSON string representation of the object
print(PlayerBattleData.to_json())

# convert the object into a dict
player_battle_data_dict = player_battle_data_instance.to_dict()
# create an instance of PlayerBattleData from a dict
player_battle_data_from_dict = PlayerBattleData.from_dict(player_battle_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


