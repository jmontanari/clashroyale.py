# clashroyale.TournamentsApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tournament**](TournamentsApi.md#get_tournament) | **GET** /tournaments/{tournamentTag} | Get tournament information
[**search_tournaments**](TournamentsApi.md#search_tournaments) | **GET** /tournaments | Search tournaments


# **get_tournament**
> Tournament get_tournament(tournament_tag)

Get tournament information

Get information about a single tournament by a tournament tag.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.tournament import Tournament
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
    api_instance = clashroyale.TournamentsApi(api_client)
    tournament_tag = 'tournament_tag_example' # str | Tag of the tournament to retrieve

    try:
        # Get tournament information
        api_response = api_instance.get_tournament(tournament_tag)
        print("The response of TournamentsApi->get_tournament:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TournamentsApi->get_tournament: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_tag** | **str**| Tag of the tournament to retrieve | 

### Return type

[**Tournament**](Tournament.md)

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

# **search_tournaments**
> List[TournamentHeader] search_tournaments(name=name, limit=limit, after=after, before=before)

Search tournaments

Search all tournaments by name. It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API.


### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.tournament_header import TournamentHeader
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
    api_instance = clashroyale.TournamentsApi(api_client)
    name = 'name_example' # str | Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  (optional)
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Search tournaments
        api_response = api_instance.search_tournaments(name=name, limit=limit, after=after, before=before)
        print("The response of TournamentsApi->search_tournaments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TournamentsApi->search_tournaments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[TournamentHeader]**](TournamentHeader.md)

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

