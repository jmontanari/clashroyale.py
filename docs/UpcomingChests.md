# UpcomingChests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Chest]**](Chest.md) |  | [optional] 

## Example

```python
from clashroyale.models.upcoming_chests import UpcomingChests

# TODO update the JSON string below
json = "{}"
# create an instance of UpcomingChests from a JSON string
upcoming_chests_instance = UpcomingChests.from_json(json)
# print the JSON string representation of the object
print(UpcomingChests.to_json())

# convert the object into a dict
upcoming_chests_dict = upcoming_chests_instance.to_dict()
# create an instance of UpcomingChests from a dict
upcoming_chests_from_dict = UpcomingChests.from_dict(upcoming_chests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


