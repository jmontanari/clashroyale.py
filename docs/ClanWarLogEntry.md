# ClanWarLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standings** | [**List[ClanWarStanding]**](ClanWarStanding.md) |  | [optional] 
**season_id** | **int** |  | [optional] 
**participants** | [**List[ClanWarParticipant]**](ClanWarParticipant.md) |  | [optional] 
**created_date** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.clan_war_log_entry import ClanWarLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ClanWarLogEntry from a JSON string
clan_war_log_entry_instance = ClanWarLogEntry.from_json(json)
# print the JSON string representation of the object
print(ClanWarLogEntry.to_json())

# convert the object into a dict
clan_war_log_entry_dict = clan_war_log_entry_instance.to_dict()
# create an instance of ClanWarLogEntry from a dict
clan_war_log_entry_from_dict = ClanWarLogEntry.from_dict(clan_war_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


