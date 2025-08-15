# Chest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**icon_urls** | **object** |  | [optional] 

## Example

```python
from clashroyale.models.chest import Chest

# TODO update the JSON string below
json = "{}"
# create an instance of Chest from a JSON string
chest_instance = Chest.from_json(json)
# print the JSON string representation of the object
print(Chest.to_json())

# convert the object into a dict
chest_dict = chest_instance.to_dict()
# create an instance of Chest from a dict
chest_from_dict = Chest.from_dict(chest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


