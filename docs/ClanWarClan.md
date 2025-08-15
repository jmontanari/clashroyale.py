# ClanWarClan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**clan_score** | **int** |  | [optional] 
**crowns** | **int** |  | [optional] 
**badge_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**participants** | **int** |  | [optional] 
**battles_played** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.clan_war_clan import ClanWarClan

# TODO update the JSON string below
json = "{}"
# create an instance of ClanWarClan from a JSON string
clan_war_clan_instance = ClanWarClan.from_json(json)
# print the JSON string representation of the object
print(ClanWarClan.to_json())

# convert the object into a dict
clan_war_clan_dict = clan_war_clan_instance.to_dict()
# create an instance of ClanWarClan from a dict
clan_war_clan_from_dict = ClanWarClan.from_dict(clan_war_clan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


