# CurrentClanWar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**clan** | [**ClanWarClan**](ClanWarClan.md) |  | [optional] 
**participants** | [**List[ClanWarParticipant]**](ClanWarParticipant.md) |  | [optional] 
**clans** | [**List[ClanWarClan]**](ClanWarClan.md) |  | [optional] 
**collection_end_time** | **str** |  | [optional] 
**war_end_time** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.current_clan_war import CurrentClanWar

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentClanWar from a JSON string
current_clan_war_instance = CurrentClanWar.from_json(json)
# print the JSON string representation of the object
print(CurrentClanWar.to_json())

# convert the object into a dict
current_clan_war_dict = current_clan_war_instance.to_dict()
# create an instance of CurrentClanWar from a dict
current_clan_war_from_dict = CurrentClanWar.from_dict(current_clan_war_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


