# Replay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replay_info** | **str** |  | [optional] 
**replay_data** | **object** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**battle_time** | **str** |  | [optional] 
**view_count** | **int** |  | [optional] 
**share_count** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.replay import Replay

# TODO update the JSON string below
json = "{}"
# create an instance of Replay from a JSON string
replay_instance = Replay.from_json(json)
# print the JSON string representation of the object
print(Replay.to_json())

# convert the object into a dict
replay_dict = replay_instance.to_dict()
# create an instance of Replay from a dict
replay_from_dict = Replay.from_dict(replay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


