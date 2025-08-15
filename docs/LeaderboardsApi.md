# clashroyale.LeaderboardsApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_leaderboard**](LeaderboardsApi.md#get_leaderboard) | **GET** /leaderboard/{leaderboardId} | Get players on a specific leaderboard
[**get_leaderboards**](LeaderboardsApi.md#get_leaderboards) | **GET** /leaderboards | List leaderboards


# **get_leaderboard**
> List[Leaderboard] get_leaderboard(leaderboard_id, limit=limit, after=after, before=before)

Get players on a specific leaderboard

Get players on a specific leaderboard

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.leaderboard import Leaderboard
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
    api_instance = clashroyale.LeaderboardsApi(api_client)
    leaderboard_id = 56 # int | A leaderboard ID from leaderboard API
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get players on a specific leaderboard
        api_response = api_instance.get_leaderboard(leaderboard_id, limit=limit, after=after, before=before)
        print("The response of LeaderboardsApi->get_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardsApi->get_leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_id** | **int**| A leaderboard ID from leaderboard API | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[Leaderboard]**](Leaderboard.md)

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

# **get_leaderboards**
> List[Leaderboard] get_leaderboards()

List leaderboards

List leaderboards for different trophy roads

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.leaderboard import Leaderboard
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
    api_instance = clashroyale.LeaderboardsApi(api_client)

    try:
        # List leaderboards
        api_response = api_instance.get_leaderboards()
        print("The response of LeaderboardsApi->get_leaderboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeaderboardsApi->get_leaderboards: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Leaderboard]**](Leaderboard.md)

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

