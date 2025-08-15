# RiverRaceClan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**clan_score** | **int** |  | [optional] 
**badge_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fame** | **int** |  | [optional] 
**repair_points** | **int** |  | [optional] 
**finish_time** | **str** |  | [optional] 
**participants** | [**List[RiverRaceParticipant]**](RiverRaceParticipant.md) |  | [optional] 
**period_points** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.river_race_clan import RiverRaceClan

# TODO update the JSON string below
json = "{}"
# create an instance of RiverRaceClan from a JSON string
river_race_clan_instance = RiverRaceClan.from_json(json)
# print the JSON string representation of the object
print(RiverRaceClan.to_json())

# convert the object into a dict
river_race_clan_dict = river_race_clan_instance.to_dict()
# create an instance of RiverRaceClan from a dict
river_race_clan_from_dict = RiverRaceClan.from_dict(river_race_clan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


