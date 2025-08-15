# RiverRaceLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**standings** | [**List[RiverRaceStanding]**](RiverRaceStanding.md) |  | [optional] 
**season_id** | **int** |  | [optional] 
**created_date** | **str** |  | [optional] 
**section_index** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.river_race_log_entry import RiverRaceLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RiverRaceLogEntry from a JSON string
river_race_log_entry_instance = RiverRaceLogEntry.from_json(json)
# print the JSON string representation of the object
print(RiverRaceLogEntry.to_json())

# convert the object into a dict
river_race_log_entry_dict = river_race_log_entry_instance.to_dict()
# create an instance of RiverRaceLogEntry from a dict
river_race_log_entry_from_dict = RiverRaceLogEntry.from_dict(river_race_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


