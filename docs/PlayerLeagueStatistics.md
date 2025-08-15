# PlayerLeagueStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_season** | [**LeagueSeasonResult**](LeagueSeasonResult.md) |  | [optional] 
**best_season** | [**LeagueSeasonResult**](LeagueSeasonResult.md) |  | [optional] 
**current_season** | [**LeagueSeasonResult**](LeagueSeasonResult.md) |  | [optional] 

## Example

```python
from clashroyale.models.player_league_statistics import PlayerLeagueStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerLeagueStatistics from a JSON string
player_league_statistics_instance = PlayerLeagueStatistics.from_json(json)
# print the JSON string representation of the object
print(PlayerLeagueStatistics.to_json())

# convert the object into a dict
player_league_statistics_dict = player_league_statistics_instance.to_dict()
# create an instance of PlayerLeagueStatistics from a dict
player_league_statistics_from_dict = PlayerLeagueStatistics.from_dict(player_league_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


