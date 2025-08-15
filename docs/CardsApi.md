# clashroyale.CardsApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cards**](CardsApi.md#get_cards) | **GET** /cards | Get list of available cards


# **get_cards**
> Items get_cards(limit=limit, after=after, before=before)

Get list of available cards

Get list of available cards

### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.items import Items
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
    api_instance = clashroyale.CardsApi(api_client)
    limit = 56 # int | Limit the number of items returned in the response. (optional)
    after = 'after_example' # str | Return only items that occur after this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)
    before = 'before_example' # str | Return only items that occur before this marker. Before marker can be found from the response, inside the 'paging' property. Note that only after or before can be specified for a request, not both.  (optional)

    try:
        # Get list of available cards
        api_response = api_instance.get_cards(limit=limit, after=after, before=before)
        print("The response of CardsApi->get_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CardsApi->get_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit the number of items returned in the response. | [optional] 
 **after** | **str**| Return only items that occur after this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 
 **before** | **str**| Return only items that occur before this marker. Before marker can be found from the response, inside the &#39;paging&#39; property. Note that only after or before can be specified for a request, not both.  | [optional] 

### Return type

[**Items**](Items.md)

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

