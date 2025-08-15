# SurvivalMilestoneReward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rarity** | **str** |  | [optional] 
**chest** | **str** |  | [optional] 
**resource** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**amount** | **int** |  | [optional] 
**card** | [**Item**](Item.md) |  | [optional] 
**consumable_name** | **str** |  | [optional] 
**wins** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.survival_milestone_reward import SurvivalMilestoneReward

# TODO update the JSON string below
json = "{}"
# create an instance of SurvivalMilestoneReward from a JSON string
survival_milestone_reward_instance = SurvivalMilestoneReward.from_json(json)
# print the JSON string representation of the object
print(SurvivalMilestoneReward.to_json())

# convert the object into a dict
survival_milestone_reward_dict = survival_milestone_reward_instance.to_dict()
# create an instance of SurvivalMilestoneReward from a dict
survival_milestone_reward_from_dict = SurvivalMilestoneReward.from_dict(survival_milestone_reward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


