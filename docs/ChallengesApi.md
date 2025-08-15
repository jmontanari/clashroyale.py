# clashroyale.ChallengesApi

All URIs are relative to *https://api.clashroyale.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_challenges**](ChallengesApi.md#get_challenges) | **GET** /challenges | Get current and upcoming challenges.


# **get_challenges**
> List[ChallengeChain] get_challenges()

Get current and upcoming challenges.

Get current and upcoming challenges. Challenges are returned as chains. Chains are either of type singleChallenge or challengeChain Possible types for prizes are: none, cardStack, chest, cardStackRandom, resource, tradeToken, consumable


### Example

* Api Key Authentication (JWT):

```python
import clashroyale
from clashroyale.models.challenge_chain import ChallengeChain
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
    api_instance = clashroyale.ChallengesApi(api_client)

    try:
        # Get current and upcoming challenges.
        api_response = api_instance.get_challenges()
        print("The response of ChallengesApi->get_challenges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChallengesApi->get_challenges: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ChallengeChain]**](ChallengeChain.md)

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

