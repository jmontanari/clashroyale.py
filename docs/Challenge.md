# Challenge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**win_mode** | **str** |  | [optional] 
**casual** | **bool** |  | [optional] 
**max_losses** | **int** |  | [optional] 
**max_wins** | **int** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**game_mode** | [**ChallengeGameMode**](ChallengeGameMode.md) |  | [optional] 
**prizes** | [**List[SurvivalMilestoneReward]**](SurvivalMilestoneReward.md) |  | [optional] 

## Example

```python
from clashroyale.models.challenge import Challenge

# TODO update the JSON string below
json = "{}"
# create an instance of Challenge from a JSON string
challenge_instance = Challenge.from_json(json)
# print the JSON string representation of the object
print(Challenge.to_json())

# convert the object into a dict
challenge_dict = challenge_instance.to_dict()
# create an instance of Challenge from a dict
challenge_from_dict = Challenge.from_dict(challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


