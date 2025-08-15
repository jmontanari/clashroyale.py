# PeriodLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PeriodLogEntry]**](PeriodLogEntry.md) |  | [optional] 
**period_index** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.period_log import PeriodLog

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodLog from a JSON string
period_log_instance = PeriodLog.from_json(json)
# print the JSON string representation of the object
print(PeriodLog.to_json())

# convert the object into a dict
period_log_dict = period_log_instance.to_dict()
# create an instance of PeriodLog from a dict
period_log_from_dict = PeriodLog.from_dict(period_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


