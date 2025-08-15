# ChallengeChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**challenges** | [**List[Challenge]**](Challenge.md) |  | [optional] 

## Example

```python
from clashroyale.models.challenge_chain import ChallengeChain

# TODO update the JSON string below
json = "{}"
# create an instance of ChallengeChain from a JSON string
challenge_chain_instance = ChallengeChain.from_json(json)
# print the JSON string representation of the object
print(ChallengeChain.to_json())

# convert the object into a dict
challenge_chain_dict = challenge_chain_instance.to_dict()
# create an instance of ChallengeChain from a dict
challenge_chain_from_dict = ChallengeChain.from_dict(challenge_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


