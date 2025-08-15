# ChallengeGameMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.challenge_game_mode import ChallengeGameMode

# TODO update the JSON string below
json = "{}"
# create an instance of ChallengeGameMode from a JSON string
challenge_game_mode_instance = ChallengeGameMode.from_json(json)
# print the JSON string representation of the object
print(ChallengeGameMode.to_json())

# convert the object into a dict
challenge_game_mode_dict = challenge_game_mode_instance.to_dict()
# create an instance of ChallengeGameMode from a dict
challenge_game_mode_from_dict = ChallengeGameMode.from_dict(challenge_game_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


