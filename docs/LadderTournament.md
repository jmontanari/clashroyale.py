# LadderTournament


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_mode** | [**GameMode**](GameMode.md) |  | [optional] 
**max_losses** | **int** |  | [optional] 
**min_exp_level** | **int** |  | [optional] 
**tournament_level** | **int** |  | [optional] 
**milestone_rewards** | [**List[SurvivalMilestoneReward]**](SurvivalMilestoneReward.md) |  | [optional] 
**free_tier_rewards** | [**List[SurvivalMilestoneReward]**](SurvivalMilestoneReward.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**top_rank_reward** | [**List[SurvivalMilestoneReward]**](SurvivalMilestoneReward.md) |  | [optional] 
**max_top_reward_rank** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.ladder_tournament import LadderTournament

# TODO update the JSON string below
json = "{}"
# create an instance of LadderTournament from a JSON string
ladder_tournament_instance = LadderTournament.from_json(json)
# print the JSON string representation of the object
print(LadderTournament.to_json())

# convert the object into a dict
ladder_tournament_dict = ladder_tournament_instance.to_dict()
# create an instance of LadderTournament from a dict
ladder_tournament_from_dict = LadderTournament.from_dict(ladder_tournament_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


