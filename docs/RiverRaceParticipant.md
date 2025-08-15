# RiverRaceParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**fame** | **int** |  | [optional] 
**repair_points** | **int** |  | [optional] 
**boat_attacks** | **int** |  | [optional] 
**decks_used** | **int** |  | [optional] 
**decks_used_today** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.river_race_participant import RiverRaceParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of RiverRaceParticipant from a JSON string
river_race_participant_instance = RiverRaceParticipant.from_json(json)
# print the JSON string representation of the object
print(RiverRaceParticipant.to_json())

# convert the object into a dict
river_race_participant_dict = river_race_participant_instance.to_dict()
# create an instance of RiverRaceParticipant from a dict
river_race_participant_from_dict = RiverRaceParticipant.from_dict(river_race_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


