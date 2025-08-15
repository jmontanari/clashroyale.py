# PlayerRankingClan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_id** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**badge_urls** | **object** |  | [optional] 

## Example

```python
from clashroyale.models.player_ranking_clan import PlayerRankingClan

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRankingClan from a JSON string
player_ranking_clan_instance = PlayerRankingClan.from_json(json)
# print the JSON string representation of the object
print(PlayerRankingClan.to_json())

# convert the object into a dict
player_ranking_clan_dict = player_ranking_clan_instance.to_dict()
# create an instance of PlayerRankingClan from a dict
player_ranking_clan_from_dict = PlayerRankingClan.from_dict(player_ranking_clan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


