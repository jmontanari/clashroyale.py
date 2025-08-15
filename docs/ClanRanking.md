# ClanRanking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clan_score** | **int** |  | [optional] 
**badge_id** | **int** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**members** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rank** | **int** |  | [optional] 
**previous_rank** | **int** |  | [optional] 
**badge_urls** | **object** |  | [optional] 

## Example

```python
from clashroyale.models.clan_ranking import ClanRanking

# TODO update the JSON string below
json = "{}"
# create an instance of ClanRanking from a JSON string
clan_ranking_instance = ClanRanking.from_json(json)
# print the JSON string representation of the object
print(ClanRanking.to_json())

# convert the object into a dict
clan_ranking_dict = clan_ranking_instance.to_dict()
# create an instance of ClanRanking from a dict
clan_ranking_from_dict = ClanRanking.from_dict(clan_ranking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


