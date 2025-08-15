# ClanWarStanding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trophy_change** | **int** |  | [optional] 
**clan** | [**ClanWarClan**](ClanWarClan.md) |  | [optional] 

## Example

```python
from clashroyale.models.clan_war_standing import ClanWarStanding

# TODO update the JSON string below
json = "{}"
# create an instance of ClanWarStanding from a JSON string
clan_war_standing_instance = ClanWarStanding.from_json(json)
# print the JSON string representation of the object
print(ClanWarStanding.to_json())

# convert the object into a dict
clan_war_standing_dict = clan_war_standing_instance.to_dict()
# create an instance of ClanWarStanding from a dict
clan_war_standing_from_dict = ClanWarStanding.from_dict(clan_war_standing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


