# clashroyale.LocationsApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clan_ranking**](LocationsApi.md#get_clan_ranking) | **GET** /locations/{locationId}/rankings/clans | Get clan rankings for a specific location
[**get_clan_wars_ranking**](LocationsApi.md#get_clan_wars_ranking) | **GET** /locations/{locationId}/rankings/clanwars | Get clan war rankings for a specific location
[**get_global_tournament_ranking**](LocationsApi.md#get_global_tournament_ranking) | **GET** /locations/global/rankings/tournaments/{tournamentTag} | Get global tournament rankings
[**get_location**](LocationsApi.md#get_location) | **GET** /locations/{locationId} | Get location information
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | List locations
[**get_player_path_of_legend_ranking**](LocationsApi.md#get_player_path_of_legend_ranking) | **GET** /locations/{locationId}/pathoflegend/players | Get player rankings in Path of Legend for a specific location
[**get_player_ranking**](LocationsApi.md#get_player_ranking) | **GET** /locations/{locationId}/rankings/players | Get player rankings for a specific location
[**get_top_player_league_season_handler**](LocationsApi.md#get_top_player_league_season_handler) | **GET** /locations/global/seasons/{seasonId} | Get top player league season.
[**get_top_player_league_season_rankings**](LocationsApi.md#get_top_player_league_season_rankings) | **GET** /locations/global/seasons/{seasonId}/rankings/players | Get top player rankings for a season.
[**get_top_player_path_of_legend_season_rankings**](LocationsApi.md#get_top_player_path_of_legend_season_rankings) | **GET** /locations/global/pathoflegend/{seasonId}/rankings/players | Get top Path of Legend players for given season.
[**list_top_player_league_seasons_handler**](LocationsApi.md#list_top_player_league_seasons_handler) | **GET** /locations/global/seasons | Lists top player league seasons.
[**list_top_player_league_seasons_v2_handler**](LocationsApi.md#list_top_player_league_seasons_v2_handler) | **GET** /locations/global/seasonsV2 | Lists league seasons with more details.


# **get_clan_ranking**
> List[ClanRanking] get_clan_ranking(location_id, limit=limit, after=after, before=before)

Get clan rankings for a specific location

Get clan rankings for a specific location

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.clan_ranking import ClanRanking
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
    api_instance = clashroyale.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get clan rankings for a specific location
        api_response = api_instance.get_clan_ranking(location_id, limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_clan_ranking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_clan_ranking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[ClanRanking]**](ClanRanking.md)

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

# **get_clan_wars_ranking**
> List[ClanRanking] get_clan_wars_ranking(location_id, limit=limit, after=after, before=before)

Get clan war rankings for a specific location

Get clan war rankings for a specific location

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.clan_ranking import ClanRanking
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
    api_instance = clashroyale.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get clan war rankings for a specific location
        api_response = api_instance.get_clan_wars_ranking(location_id, limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_clan_wars_ranking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_clan_wars_ranking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[ClanRanking]**](ClanRanking.md)

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

# **get_global_tournament_ranking**
> List[LadderTournamentRanking] get_global_tournament_ranking(tournament_tag, limit=limit, after=after, before=before)

Get global tournament rankings

Get global tournament rankings

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.ladder_tournament_ranking import LadderTournamentRanking
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
    api_instance = clashroyale.LocationsApi(api_client)
    tournament_tag = 'tournament_tag_example' # str | Tag of the tournament to retrieve
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get global tournament rankings
        api_response = api_instance.get_global_tournament_ranking(tournament_tag, limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_global_tournament_ranking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_global_tournament_ranking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_tag** | **str**| Tag of the tournament to retrieve | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[LadderTournamentRanking]**](LadderTournamentRanking.md)

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

# **get_location**
> Location get_location(location_id)

Get location information

Get information about specific location

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.location import Location
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
    api_instance = clashroyale.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.

    try:
        # Get location information
        api_response = api_instance.get_location(location_id)
        print("The response of LocationsApi->get_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 

### Return type

[**Location**](Location.md)

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

# **get_locations**
> List[Location] get_locations(limit=limit, after=after, before=before)

List locations

List locations

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.location import Location
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
    api_instance = clashroyale.LocationsApi(api_client)
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # List locations
        api_response = api_instance.get_locations(limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[Location]**](Location.md)

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

# **get_player_path_of_legend_ranking**
> List[PlayerPathOfLegendRanking] get_player_path_of_legend_ranking(location_id, limit=limit, after=after, before=before)

Get player rankings in Path of Legend for a specific location

Get player rankings in Path of Legend for a specific location

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.player_path_of_legend_ranking import PlayerPathOfLegendRanking
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
    api_instance = clashroyale.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get player rankings in Path of Legend for a specific location
        api_response = api_instance.get_player_path_of_legend_ranking(location_id, limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_player_path_of_legend_ranking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_player_path_of_legend_ranking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[PlayerPathOfLegendRanking]**](PlayerPathOfLegendRanking.md)

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

# **get_player_ranking**
> List[PlayerRanking] get_player_ranking(location_id, limit=limit, after=after, before=before)

Get player rankings for a specific location

Get player rankings for a specific location

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.player_ranking import PlayerRanking
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
    api_instance = clashroyale.LocationsApi(api_client)
    location_id = 'location_id_example' # str | Identifier of the location to retrieve.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get player rankings for a specific location
        api_response = api_instance.get_player_ranking(location_id, limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_player_ranking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_player_ranking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location_id** | **str**| Identifier of the location to retrieve. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[PlayerRanking]**](PlayerRanking.md)

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

# **get_top_player_league_season_handler**
> LeagueSeason get_top_player_league_season_handler(season_id)

Get top player league season.

Get top player league season.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.league_season import LeagueSeason
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
    api_instance = clashroyale.LocationsApi(api_client)
    season_id = 'season_id_example' # str | Identifier of the season.

    try:
        # Get top player league season.
        api_response = api_instance.get_top_player_league_season_handler(season_id)
        print("The response of LocationsApi->get_top_player_league_season_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_top_player_league_season_handler: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **str**| Identifier of the season. | 

### Return type

[**LeagueSeason**](LeagueSeason.md)

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

# **get_top_player_league_season_rankings**
> List[PlayerRanking] get_top_player_league_season_rankings(season_id, limit=limit, after=after, before=before)

Get top player rankings for a season.

Get top player rankings for a season.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.player_ranking import PlayerRanking
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
    api_instance = clashroyale.LocationsApi(api_client)
    season_id = 'season_id_example' # str | Identifier of the season.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get top player rankings for a season.
        api_response = api_instance.get_top_player_league_season_rankings(season_id, limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_top_player_league_season_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_top_player_league_season_rankings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **str**| Identifier of the season. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[PlayerRanking]**](PlayerRanking.md)

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

# **get_top_player_path_of_legend_season_rankings**
> List[PlayerPathOfLegendRanking] get_top_player_path_of_legend_season_rankings(season_id, limit=limit, after=after, before=before)

Get top Path of Legend players for given season.

Get top Path of Legend players for given season.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.player_path_of_legend_ranking import PlayerPathOfLegendRanking
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
    api_instance = clashroyale.LocationsApi(api_client)
    season_id = 'season_id_example' # str | Identifier of the season.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get top Path of Legend players for given season.
        api_response = api_instance.get_top_player_path_of_legend_season_rankings(season_id, limit=limit, after=after, before=before)
        print("The response of LocationsApi->get_top_player_path_of_legend_season_rankings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_top_player_path_of_legend_season_rankings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **str**| Identifier of the season. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[PlayerPathOfLegendRanking]**](PlayerPathOfLegendRanking.md)

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

# **list_top_player_league_seasons_handler**
> List[LeagueSeason] list_top_player_league_seasons_handler()

Lists top player league seasons.

Lists top player league seasons.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.league_season import LeagueSeason
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
    api_instance = clashroyale.LocationsApi(api_client)

    try:
        # Lists top player league seasons.
        api_response = api_instance.list_top_player_league_seasons_handler()
        print("The response of LocationsApi->list_top_player_league_seasons_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->list_top_player_league_seasons_handler: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LeagueSeason]**](LeagueSeason.md)

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

# **list_top_player_league_seasons_v2_handler**
> List[LeagueSeason] list_top_player_league_seasons_v2_handler()

Lists league seasons with more details.

Lists league seasons with unique season IDs and season end times.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.league_season import LeagueSeason
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
    api_instance = clashroyale.LocationsApi(api_client)

    try:
        # Lists league seasons with more details.
        api_response = api_instance.list_top_player_league_seasons_v2_handler()
        print("The response of LocationsApi->list_top_player_league_seasons_v2_handler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->list_top_player_league_seasons_v2_handler: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LeagueSeason]**](LeagueSeason.md)

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

