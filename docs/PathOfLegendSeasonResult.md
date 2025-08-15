# PathOfLegendSeasonResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trophies** | **int** |  | [optional] 
**rank** | **int** |  | [optional] 
**league_number** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.path_of_legend_season_result import PathOfLegendSeasonResult

# TODO update the JSON string below
json = "{}"
# create an instance of PathOfLegendSeasonResult from a JSON string
path_of_legend_season_result_instance = PathOfLegendSeasonResult.from_json(json)
# print the JSON string representation of the object
print(PathOfLegendSeasonResult.to_json())

# convert the object into a dict
path_of_legend_season_result_dict = path_of_legend_season_result_instance.to_dict()
# create an instance of PathOfLegendSeasonResult from a dict
path_of_legend_season_result_from_dict = PathOfLegendSeasonResult.from_dict(path_of_legend_season_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


