## GET SNAPSHOT QUERY STRING

Command that is initiated in Composer Pro and immediately returns a block of XML information. It returns the query string needed to create the URL for HTTP snapshot request.


### Signature

`GET_SNAPSHOT_QUERY_STRING ()`


| Parameter | Description |
| --- | --- |
| SIZE_X | The desired resolution x-axis value. |
| SIZE_Y | The desired resolution y-axis value. |


### Returns

XML: `<snapshot_query_string>url-query-string</snapshot_query_string>`