# ClanMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arena** | [**Arena**](Arena.md) |  | [optional] 
**clan_chest_points** | **int** |  | [optional] 
**last_seen** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**exp_level** | **int** |  | [optional] 
**trophies** | **int** |  | [optional] 
**clan_rank** | **int** |  | [optional] 
**previous_clan_rank** | **int** |  | [optional] 
**donations** | **int** |  | [optional] 
**donations_received** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.clan_member import ClanMember

# TODO update the JSON string below
json = "{}"
# create an instance of ClanMember from a JSON string
clan_member_instance = ClanMember.from_json(json)
# print the JSON string representation of the object
print(ClanMember.to_json())

# convert the object into a dict
clan_member_dict = clan_member_instance.to_dict()
# create an instance of ClanMember from a dict
clan_member_from_dict = ClanMember.from_dict(clan_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


