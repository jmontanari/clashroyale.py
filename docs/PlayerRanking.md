# PlayerRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan** | [**PlayerRankingClan**](PlayerRankingClan.md) |  | [optional] 
**arena** | [**Arena**](Arena.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**exp_level** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**previous_rank** | **int** |  | [optional] 
**trophies** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.player_ranking import PlayerRanking

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRanking from a JSON string
player_ranking_instance = PlayerRanking.from_json(json)
# print the JSON string representation of the object
print(PlayerRanking.to_json())

# convert the object into a dict
player_ranking_dict = player_ranking_instance.to_dict()
# create an instance of PlayerRanking from a dict
player_ranking_from_dict = PlayerRanking.from_dict(player_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


