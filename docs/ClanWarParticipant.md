# ClanWarParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**cards_earned** | **int** |  | [optional] 
**battles_played** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**collection_day_battles_played** | **int** |  | [optional] 
**number_of_battles** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.clan_war_participant import ClanWarParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of ClanWarParticipant from a JSON string
clan_war_participant_instance = ClanWarParticipant.from_json(json)
# print the JSON string representation of the object
print(ClanWarParticipant.to_json())

# convert the object into a dict
clan_war_participant_dict = clan_war_participant_instance.to_dict()
# create an instance of ClanWarParticipant from a dict
clan_war_participant_from_dict = ClanWarParticipant.from_dict(clan_war_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


