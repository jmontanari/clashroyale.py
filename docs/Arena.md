# Arena


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**icon_urls** | **object** |  | [optional] 

## Example

```python
from clashroyale.models.arena import Arena

# TODO update the JSON string below
json = "{}"
# create an instance of Arena from a JSON string
arena_instance = Arena.from_json(json)
# print the JSON string representation of the object
print(Arena.to_json())

# convert the object into a dict
arena_dict = arena_instance.to_dict()
# create an instance of Arena from a dict
arena_from_dict = Arena.from_dict(arena_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


