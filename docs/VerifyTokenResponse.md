# VerifyTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from clashroyale.models.verify_token_response import VerifyTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTokenResponse from a JSON string
verify_token_response_instance = VerifyTokenResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyTokenResponse.to_json())

# convert the object into a dict
verify_token_response_dict = verify_token_response_instance.to_dict()
# create an instance of VerifyTokenResponse from a dict
verify_token_response_from_dict = VerifyTokenResponse.from_dict(verify_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


