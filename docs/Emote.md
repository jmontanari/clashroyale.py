# Emote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**index_hi** | **int** |  | [optional] 
**index_lo** | **int** |  | [optional] 
**available** | **bool** |  | [optional] 
**default_owned** | **bool** |  | [optional] 
**sfx_file** | **str** |  | [optional] 
**sc_file** | **str** |  | [optional] 
**available_for_offer** | **bool** |  | [optional] 
**exclusive** | **bool** |  | [optional] 
**date_available** | **str** |  | [optional] 
**human_readable_name** | **str** |  | [optional] 
**family** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.emote import Emote

# TODO update the JSON string below
json = "{}"
# create an instance of Emote from a JSON string
emote_instance = Emote.from_json(json)
# print the JSON string representation of the object
print(Emote.to_json())

# convert the object into a dict
emote_dict = emote_instance.to_dict()
# create an instance of Emote from a dict
emote_from_dict = Emote.from_dict(emote_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


