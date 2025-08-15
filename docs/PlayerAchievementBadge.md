# PlayerAchievementBadge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_urls** | **object** |  | [optional] 
**max_level** | **int** |  | [optional] 
**progress** | **int** |  | [optional] 
**target** | **int** |  | [optional] 
**level** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.player_achievement_badge import PlayerAchievementBadge

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerAchievementBadge from a JSON string
player_achievement_badge_instance = PlayerAchievementBadge.from_json(json)
# print the JSON string representation of the object
print(PlayerAchievementBadge.to_json())

# convert the object into a dict
player_achievement_badge_dict = player_achievement_badge_instance.to_dict()
# create an instance of PlayerAchievementBadge from a dict
player_achievement_badge_from_dict = PlayerAchievementBadge.from_dict(player_achievement_badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


