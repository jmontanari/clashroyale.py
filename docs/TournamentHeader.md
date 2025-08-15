# TournamentHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**preparation_duration** | **int** |  | [optional] 
**created_time** | **str** |  | [optional] 
**first_place_card_prize** | **int** |  | [optional] 
**game_mode** | [**GameMode**](GameMode.md) |  | [optional] 
**duration** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**creator_tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**capacity** | **int** |  | [optional] 
**max_capacity** | **int** |  | [optional] 
**level_cap** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.tournament_header import TournamentHeader

# TODO update the JSON string below
json = "{}"
# create an instance of TournamentHeader from a JSON string
tournament_header_instance = TournamentHeader.from_json(json)
# print the JSON string representation of the object
print(TournamentHeader.to_json())

# convert the object into a dict
tournament_header_dict = tournament_header_instance.to_dict()
# create an instance of TournamentHeader from a dict
tournament_header_from_dict = TournamentHeader.from_dict(tournament_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


