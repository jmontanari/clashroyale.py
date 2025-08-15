# Fingerprint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**files** | **List[object]** |  | [optional] 

## Example

```python
from clashroyale.models.fingerprint import Fingerprint

# TODO update the JSON string below
json = "{}"
# create an instance of Fingerprint from a JSON string
fingerprint_instance = Fingerprint.from_json(json)
# print the JSON string representation of the object
print(Fingerprint.to_json())

# convert the object into a dict
fingerprint_dict = fingerprint_instance.to_dict()
# create an instance of Fingerprint from a dict
fingerprint_from_dict = Fingerprint.from_dict(fingerprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


