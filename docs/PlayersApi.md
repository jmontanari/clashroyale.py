# clashroyale.PlayersApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{playerTag} | Get player information
[**get_player_battles**](PlayersApi.md#get_player_battles) | **GET** /players/{playerTag}/battlelog | Get list of recent battles for a player
[**get_player_upcoming_chests**](PlayersApi.md#get_player_upcoming_chests) | **GET** /players/{playerTag}/upcomingchests | Get information about player&#39;s upcoming chests


# **get_player**
> Player get_player(player_tag)

Get player information

Get information about a single player by player tag. Player tags can be found either in game or by from clan member lists. Note that player tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example player tag '#2ABC' would become '%232ABC' in the URL.


### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.player import Player
from clashroyale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.clashroyale.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clashroyale.Configuration(
    host = "https://api.clashroyale.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with clashroyale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clashroyale.PlayersApi(api_client)
    player_tag = 'player_tag_example' # str | Tag of the player.

    try:
        # Get player information
        api_response = api_instance.get_player(player_tag)
        print("The response of PlayersApi->get_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**Player**](Player.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request. |  -  |
**503** | Service is temprorarily unavailable because of maintenance. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_battles**
> List[Battle] get_player_battles(player_tag)

Get list of recent battles for a player

Get list of recent battles for a player

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.battle import Battle
from clashroyale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.clashroyale.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clashroyale.Configuration(
    host = "https://api.clashroyale.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with clashroyale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clashroyale.PlayersApi(api_client)
    player_tag = 'player_tag_example' # str | Tag of the player.

    try:
        # Get list of recent battles for a player
        api_response = api_instance.get_player_battles(player_tag)
        print("The response of PlayersApi->get_player_battles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player_battles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**List[Battle]**](Battle.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request. |  -  |
**503** | Service is temprorarily unavailable because of maintenance. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_upcoming_chests**
> UpcomingChests get_player_upcoming_chests(player_tag)

Get information about player's upcoming chests

Get list of reward chests that the player will receive next in the game.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.upcoming_chests import UpcomingChests
from clashroyale.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.clashroyale.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = clashroyale.Configuration(
    host = "https://api.clashroyale.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with clashroyale.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clashroyale.PlayersApi(api_client)
    player_tag = 'player_tag_example' # str | Tag of the player.

    try:
        # Get information about player's upcoming chests
        api_response = api_instance.get_player_upcoming_chests(player_tag)
        print("The response of PlayersApi->get_player_upcoming_chests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlayersApi->get_player_upcoming_chests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_tag** | **str**| Tag of the player. | 

### Return type

[**UpcomingChests**](UpcomingChests.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Client provided incorrect parameters for the request. |  -  |
**403** | Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.  |  -  |
**404** | Resource was not found. |  -  |
**429** | Request was throttled, because amount of requests was above the threshold defined for the used API token.  |  -  |
**500** | Unknown error happened when handling the request. |  -  |
**503** | Service is temprorarily unavailable because of maintenance. |  -  |
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

