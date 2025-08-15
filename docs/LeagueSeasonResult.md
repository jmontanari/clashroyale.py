# LeagueSeasonResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trophies** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**best_trophies** | **int** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.league_season_result import LeagueSeasonResult

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueSeasonResult from a JSON string
league_season_result_instance = LeagueSeasonResult.from_json(json)
# print the JSON string representation of the object
print(LeagueSeasonResult.to_json())

# convert the object into a dict
league_season_result_dict = league_season_result_instance.to_dict()
# create an instance of LeagueSeasonResult from a dict
league_season_result_from_dict = LeagueSeasonResult.from_dict(league_season_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


