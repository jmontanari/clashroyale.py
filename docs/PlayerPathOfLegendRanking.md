# PlayerPathOfLegendRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan** | [**PlayerRankingClan**](PlayerRankingClan.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**exp_level** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**elo_rating** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.player_path_of_legend_ranking import PlayerPathOfLegendRanking

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerPathOfLegendRanking from a JSON string
player_path_of_legend_ranking_instance = PlayerPathOfLegendRanking.from_json(json)
# print the JSON string representation of the object
print(PlayerPathOfLegendRanking.to_json())

# convert the object into a dict
player_path_of_legend_ranking_dict = player_path_of_legend_ranking_instance.to_dict()
# create an instance of PlayerPathOfLegendRanking from a dict
player_path_of_legend_ranking_from_dict = PlayerPathOfLegendRanking.from_dict(player_path_of_legend_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


