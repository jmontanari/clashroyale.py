# PlayerItemLevel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**rarity** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**level** | **int** |  | [optional] 
**star_level** | **int** |  | [optional] 
**evolution_level** | **int** |  | [optional] 
**used** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**max_level** | **int** |  | [optional] 
**elixir_cost** | **int** |  | [optional] 
**max_evolution_level** | **int** |  | [optional] 
**icon_urls** | **object** |  | [optional] 

## Example

```python
from clashroyale.models.player_item_level import PlayerItemLevel

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerItemLevel from a JSON string
player_item_level_instance = PlayerItemLevel.from_json(json)
# print the JSON string representation of the object
print(PlayerItemLevel.to_json())

# convert the object into a dict
player_item_level_dict = player_item_level_instance.to_dict()
# create an instance of PlayerItemLevel from a dict
player_item_level_from_dict = PlayerItemLevel.from_dict(player_item_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


