# RiverRaceStanding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | [optional] 
**trophy_change** | **int** |  | [optional] 
**clan** | [**RiverRaceClan**](RiverRaceClan.md) |  | [optional] 

## Example

```python
from clashroyale.models.river_race_standing import RiverRaceStanding

# TODO update the JSON string below
json = "{}"
# create an instance of RiverRaceStanding from a JSON string
river_race_standing_instance = RiverRaceStanding.from_json(json)
# print the JSON string representation of the object
print(RiverRaceStanding.to_json())

# convert the object into a dict
river_race_standing_dict = river_race_standing_instance.to_dict()
# create an instance of RiverRaceStanding from a dict
river_race_standing_from_dict = RiverRaceStanding.from_dict(river_race_standing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


