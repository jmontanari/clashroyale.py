# LadderTournamentRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan** | [**PlayerRankingClan**](PlayerRankingClan.md) |  | [optional] 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rank** | **int** |  | [optional] 
**previous_rank** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.ladder_tournament_ranking import LadderTournamentRanking

# TODO update the JSON string below
json = "{}"
# create an instance of LadderTournamentRanking from a JSON string
ladder_tournament_ranking_instance = LadderTournamentRanking.from_json(json)
# print the JSON string representation of the object
print(LadderTournamentRanking.to_json())

# convert the object into a dict
ladder_tournament_ranking_dict = ladder_tournament_ranking_instance.to_dict()
# create an instance of LadderTournamentRanking from a dict
ladder_tournament_ranking_from_dict = LadderTournamentRanking.from_dict(ladder_tournament_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


