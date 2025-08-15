# clashroyale.ClansApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_clan**](ClansApi.md#get_clan) | **GET** /clans/{clanTag} | Get clan information
[**get_clan_members**](ClansApi.md#get_clan_members) | **GET** /clans/{clanTag}/members | List clan members
[**get_clan_war_log**](ClansApi.md#get_clan_war_log) | **GET** /clans/{clanTag}/warlog | Retrieve clan&#39;s clan war log
[**get_current_river_race**](ClansApi.md#get_current_river_race) | **GET** /clans/{clanTag}/currentriverrace | Retrieve information about clan&#39;s current river race
[**get_current_war**](ClansApi.md#get_current_war) | **GET** /clans/{clanTag}/currentwar | Retrieve information about clan&#39;s current clan war
[**get_river_race_war_log**](ClansApi.md#get_river_race_war_log) | **GET** /clans/{clanTag}/riverracelog | Retrieve clan&#39;s river race log
[**search_clans**](ClansApi.md#search_clans) | **GET** /clans | Search clans


# **get_clan**
> Clan get_clan(clan_tag)

Get clan information

Get information about a single clan by clan tag. Clan tags can be found using clan search operation. Note that clan tags start with hash character '#' and that needs to be URL-encoded properly to work in URL, so for example clan tag '#2ABC' would become '%232ABC' in the URL.


### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.clan import Clan
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
    api_instance = clashroyale.ClansApi(api_client)
    clan_tag = 'clan_tag_example' # str | Tag of the clan.

    try:
        # Get clan information
        api_response = api_instance.get_clan(clan_tag)
        print("The response of ClansApi->get_clan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 

### Return type

[**Clan**](Clan.md)

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

# **get_clan_members**
> List[ClanMember] get_clan_members(clan_tag, limit=limit, after=after, before=before)

List clan members

List clan members.

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.clan_member import ClanMember
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
    api_instance = clashroyale.ClansApi(api_client)
    clan_tag = 'clan_tag_example' # str | Tag of the clan.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # List clan members
        api_response = api_instance.get_clan_members(clan_tag, limit=limit, after=after, before=before)
        print("The response of ClansApi->get_clan_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clan_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[ClanMember]**](ClanMember.md)

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

# **get_clan_war_log**
> List[ClanWarLogEntry] get_clan_war_log(clan_tag, limit=limit, after=after, before=before)

Retrieve clan's clan war log

Retrieve clan's clan war log

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.clan_war_log_entry import ClanWarLogEntry
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
    api_instance = clashroyale.ClansApi(api_client)
    clan_tag = 'clan_tag_example' # str | Tag of the clan.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Retrieve clan's clan war log
        api_response = api_instance.get_clan_war_log(clan_tag, limit=limit, after=after, before=before)
        print("The response of ClansApi->get_clan_war_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_clan_war_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[ClanWarLogEntry]**](ClanWarLogEntry.md)

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

# **get_current_river_race**
> CurrentRiverRace get_current_river_race(clan_tag)

Retrieve information about clan's current river race

Retrieve information about clan's current river race

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.current_river_race import CurrentRiverRace
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
    api_instance = clashroyale.ClansApi(api_client)
    clan_tag = 'clan_tag_example' # str | Tag of the clan.

    try:
        # Retrieve information about clan's current river race
        api_response = api_instance.get_current_river_race(clan_tag)
        print("The response of ClansApi->get_current_river_race:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_current_river_race: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 

### Return type

[**CurrentRiverRace**](CurrentRiverRace.md)

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

# **get_current_war**
> CurrentClanWar get_current_war(clan_tag)

Retrieve information about clan's current clan war

Retrieve information about clan's current clan war

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.current_clan_war import CurrentClanWar
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
    api_instance = clashroyale.ClansApi(api_client)
    clan_tag = 'clan_tag_example' # str | Tag of the clan.

    try:
        # Retrieve information about clan's current clan war
        api_response = api_instance.get_current_war(clan_tag)
        print("The response of ClansApi->get_current_war:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_current_war: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 

### Return type

[**CurrentClanWar**](CurrentClanWar.md)

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

# **get_river_race_war_log**
> List[RiverRaceLogEntry] get_river_race_war_log(clan_tag, limit=limit, after=after, before=before)

Retrieve clan's river race log

Retrieve clan's river race log

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.river_race_log_entry import RiverRaceLogEntry
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
    api_instance = clashroyale.ClansApi(api_client)
    clan_tag = 'clan_tag_example' # str | Tag of the clan.
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Retrieve clan's river race log
        api_response = api_instance.get_river_race_war_log(clan_tag, limit=limit, after=after, before=before)
        print("The response of ClansApi->get_river_race_war_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->get_river_race_war_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clan_tag** | **str**| Tag of the clan. | 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[RiverRaceLogEntry]**](RiverRaceLogEntry.md)

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

# **search_clans**
> List[Clan] search_clans(name=name, location_id=location_id, min_members=min_members, max_members=max_members, min_score=min_score, limit=limit, after=after, before=before)

Search clans

Search all clans by name and/or filtering the results using various criteria. At least one filtering criteria must be defined and if name is used as part of search, it is required to be at least three characters long It is not possible to specify ordering for results so clients should not rely on any specific ordering as that may change in the future releases of the API.


### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.clan import Clan
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
    api_instance = clashroyale.ClansApi(api_client)
    name = 'name_example' # str | Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  (optional)
    location_id = 56 # int | Filter by clan location identifier. For list of available locations, refer to getLocations operation.  (optional)
    min_members = 56 # int | Filter by minimum number of clan members (optional)
    max_members = 56 # int | Filter by maximum number of clan members (optional)
    min_score = 56 # int | Filter by minimum amount of clan score. (optional)
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Search clans
        api_response = api_instance.search_clans(name=name, location_id=location_id, min_members=min_members, max_members=max_members, min_score=min_score, limit=limit, after=after, before=before)
        print("The response of ClansApi->search_clans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClansApi->search_clans: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Search clans by name. If name is used as part of search query, it needs to be at least three characters long. Name search parameter is interpreted as wild card search, so it may appear anywhere in the clan name.  | [optional] 
 **location_id** | **int**| Filter by clan location identifier. For list of available locations, refer to getLocations operation.  | [optional] 
 **min_members** | **int**| Filter by minimum number of clan members | [optional] 
 **max_members** | **int**| Filter by maximum number of clan members | [optional] 
 **min_score** | **int**| Filter by minimum amount of clan score. | [optional] 
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**List[Clan]**](Clan.md)

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

