# CurrentRiverRace


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**clan** | [**RiverRaceClan**](RiverRaceClan.md) |  | [optional] 
**clans** | [**List[RiverRaceClan]**](RiverRaceClan.md) |  | [optional] 
**collection_end_time** | **str** |  | [optional] 
**war_end_time** | **str** |  | [optional] 
**section_index** | **int** |  | [optional] 
**period_index** | **int** |  | [optional] 
**period_type** | **str** |  | [optional] 
**period_logs** | [**List[PeriodLog]**](PeriodLog.md) |  | [optional] 

## Example

```python
from clashroyale.models.current_river_race import CurrentRiverRace

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentRiverRace from a JSON string
current_river_race_instance = CurrentRiverRace.from_json(json)
# print the JSON string representation of the object
print(CurrentRiverRace.to_json())

# convert the object into a dict
current_river_race_dict = current_river_race_instance.to_dict()
# create an instance of CurrentRiverRace from a dict
current_river_race_from_dict = CurrentRiverRace.from_dict(current_river_race_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


