# swagger_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_get**](DefaultApi.md#query_get) | **GET** /query/ | Query metadata for matching APIs.
[**suggestion_get**](DefaultApi.md#suggestion_get) | **GET** /suggestion | Return suggested values for a give field.
[**validate_get**](DefaultApi.md#validate_get) | **GET** /validate | Validate input SmartAPI metadata


# **query_get**
> query_get(q, fields=fields, raw=raw)

Query metadata for matching APIs.

Query metadata for matching APIs.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
q = 'q_example' # str | Can pass any string as the query term to match any field, e.g. \"mygene.info\", or pass a fielded query term like \"info.contact.name:wu\".
fields = 'fields_example' # str | You can use this parameter to filter the fields returned from the raw metadata document. Only effective when \"raw=1\" is passed. E.g. \"info.contact.name,servers\". Nested fields are supported via dot notation, and multiple fields can be passed as a comma-separated string. (optional)
raw = 'raw_example' # str | return raw metadata document if passed \"1\" or \"true\". Default is \"false\". (optional)

try:
    # Query metadata for matching APIs.
    api_instance.query_get(q, fields=fields, raw=raw)
except ApiException as e:
    print("Exception when calling DefaultApi->query_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Can pass any string as the query term to match any field, e.g. \&quot;mygene.info\&quot;, or pass a fielded query term like \&quot;info.contact.name:wu\&quot;. | 
 **fields** | **str**| You can use this parameter to filter the fields returned from the raw metadata document. Only effective when \&quot;raw&#x3D;1\&quot; is passed. E.g. \&quot;info.contact.name,servers\&quot;. Nested fields are supported via dot notation, and multiple fields can be passed as a comma-separated string. | [optional] 
 **raw** | **str**| return raw metadata document if passed \&quot;1\&quot; or \&quot;true\&quot;. Default is \&quot;false\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggestion_get**
> suggestion_get(field=field, size=size)

Return suggested values for a give field.

Return suggested values from the existing APIs in the registry for a given field.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
field = 'field_example' # str | An input field to return the suggested values and their occurrence numbers. (optional)
size = 'size_example' # str | The maximum number of suggested values to return (optional)

try:
    # Return suggested values for a give field.
    api_instance.suggestion_get(field=field, size=size)
except ApiException as e:
    print("Exception when calling DefaultApi->suggestion_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| An input field to return the suggested values and their occurrence numbers. | [optional] 
 **size** | **str**| The maximum number of suggested values to return | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_get**
> validate_get(url)

Validate input SmartAPI metadata

Validate input SmartAPI metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
url = 'url_example' # str | The full URL of an input SmartAPI metadata to validate. The file format can be either JSON or YAML.

try:
    # Validate input SmartAPI metadata
    api_instance.validate_get(url)
except ApiException as e:
    print("Exception when calling DefaultApi->validate_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| The full URL of an input SmartAPI metadata to validate. The file format can be either JSON or YAML. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

