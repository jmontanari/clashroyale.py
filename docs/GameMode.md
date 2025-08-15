# GameMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.game_mode import GameMode

# TODO update the JSON string below
json = "{}"
# create an instance of GameMode from a JSON string
game_mode_instance = GameMode.from_json(json)
# print the JSON string representation of the object
print(GameMode.to_json())

# convert the object into a dict
game_mode_dict = game_mode_instance.to_dict()
# create an instance of GameMode from a dict
game_mode_from_dict = GameMode.from_dict(game_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


