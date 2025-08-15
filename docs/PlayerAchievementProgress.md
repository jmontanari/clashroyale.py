# PlayerAchievementProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stars** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**target** | **int** |  | [optional] 
**info** | **str** |  | [optional] 
**completion_info** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.player_achievement_progress import PlayerAchievementProgress

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerAchievementProgress from a JSON string
player_achievement_progress_instance = PlayerAchievementProgress.from_json(json)
# print the JSON string representation of the object
print(PlayerAchievementProgress.to_json())

# convert the object into a dict
player_achievement_progress_dict = player_achievement_progress_instance.to_dict()
# create an instance of PlayerAchievementProgress from a dict
player_achievement_progress_from_dict = PlayerAchievementProgress.from_dict(player_achievement_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


