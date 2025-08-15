# TournamentMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | [optional] 
**clan** | [**PlayerClan**](PlayerClan.md) |  | [optional] 
**previous_rank** | **int** |  | [optional] 
**tag** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**score** | **int** |  | [optional] 

## Example

```python
from clashroyale.models.tournament_member import TournamentMember

# TODO update the JSON string below
json = "{}"
# create an instance of TournamentMember from a JSON string
tournament_member_instance = TournamentMember.from_json(json)
# print the JSON string representation of the object
print(TournamentMember.to_json())

# convert the object into a dict
tournament_member_dict = tournament_member_instance.to_dict()
# create an instance of TournamentMember from a dict
tournament_member_from_dict = TournamentMember.from_dict(tournament_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


