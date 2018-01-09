# swagger_client.MetadataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadata_api_id_get**](MetadataApi.md#metadata_api_id_get) | **GET** /metadata/{api_id} | Return matching API metadata


# **metadata_api_id_get**
> metadata_api_id_get(api_id, meta=meta, raw=raw, fields=fields, _from=_from, size=size)

Return matching API metadata

Return matching API metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()
api_id = 'api_id_example' # str | 
meta = 'meta_example' # str | include \"_meta\" and \"_id\" fields in the response if passed \"1\" or \"true\". Default is \"false\". (optional)
raw = 'raw_example' # str | return raw metadata document if passed \"1\" or \"true\". Default is \"false\". (optional)
fields = 'fields_example' # str | You can use this parameter to filter the fields returned from the raw metadata document. Only effective when \"raw=1\" is passed. E.g. \"info.contact.name,servers\". Nested fields are supported via dot notation, and multiple fields can be passed as a comma-separated string. (optional)
_from = '_from_example' # str | Number of items to be skipped. Combining with \"size\" parameter, this can be used for the pagination of the long result. (optional)
size = 'size_example' # str | The number of items returned in one request. Combining with \"from\" parameter, this can be used for the pagination of the long result. (optional)

try:
    # Return matching API metadata
    api_instance.metadata_api_id_get(api_id, meta=meta, raw=raw, fields=fields, _from=_from, size=size)
except ApiException as e:
    print("Exception when calling MetadataApi->metadata_api_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**|  | 
 **meta** | **str**| include \&quot;_meta\&quot; and \&quot;_id\&quot; fields in the response if passed \&quot;1\&quot; or \&quot;true\&quot;. Default is \&quot;false\&quot;. | [optional] 
 **raw** | **str**| return raw metadata document if passed \&quot;1\&quot; or \&quot;true\&quot;. Default is \&quot;false\&quot;. | [optional] 
 **fields** | **str**| You can use this parameter to filter the fields returned from the raw metadata document. Only effective when \&quot;raw&#x3D;1\&quot; is passed. E.g. \&quot;info.contact.name,servers\&quot;. Nested fields are supported via dot notation, and multiple fields can be passed as a comma-separated string. | [optional] 
 **_from** | **str**| Number of items to be skipped. Combining with \&quot;size\&quot; parameter, this can be used for the pagination of the long result. | [optional] 
 **size** | **str**| The number of items returned in one request. Combining with \&quot;from\&quot; parameter, this can be used for the pagination of the long result. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

