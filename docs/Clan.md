# Clan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_list** | [**List[ClanMember]**](ClanMember.md) |  | [optional] 
**tag** | **str** |  | [optional] 
**clan_score** | **int** |  | [optional] 
**clan_chest_max_level** | **int** |  | [optional] 
**clan_war_trophies** | **int** |  | [optional] 
**required_trophies** | **int** |  | [optional] 
**donations_per_week** | **int** |  | [optional] 
**badge_id** | **int** |  | [optional] 
**clan_chest_status** | **str** |  | [optional] 
**clan_chest_level** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**type** | **str** |  | [optional] 
**members** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**clan_chest_points** | **int** |  | [optional] 
**badge_urls** | **object** |  | [optional] 

## Example

```python
from clashroyale.models.clan import Clan

# TODO update the JSON string below
json = "{}"
# create an instance of Clan from a JSON string
clan_instance = Clan.from_json(json)
# print the JSON string representation of the object
print(Clan.to_json())

# convert the object into a dict
clan_dict = clan_instance.to_dict()
# create an instance of Clan from a dict
clan_from_dict = Clan.from_dict(clan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


