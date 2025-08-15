# Tournament


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members_list** | [**List[TournamentMember]**](TournamentMember.md) |  | [optional] 
**status** | **str** |  | [optional] 
**preparation_duration** | **int** |  | [optional] 
**created_time** | **str** |  | [optional] 
**started_time** | **str** |  | [optional] 
**ended_time** | **str** |  | [optional] 
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
from clashroyale.models.tournament import Tournament

# TODO update the JSON string below
json = "{}"
# create an instance of Tournament from a JSON string
tournament_instance = Tournament.from_json(json)
# print the JSON string representation of the object
print(Tournament.to_json())

# convert the object into a dict
tournament_dict = tournament_instance.to_dict()
# create an instance of Tournament from a dict
tournament_from_dict = Tournament.from_dict(tournament_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


