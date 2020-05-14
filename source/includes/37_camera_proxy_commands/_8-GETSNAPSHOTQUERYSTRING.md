## GET SNAPSHOT4 QUERY STRING

Command that is initiated in Composer Pro and immediately returns a block of XML information. It returns the query string needed to create the URL for HTTP snapshot request.


### Signature

`C4:GET_SNAPSHOT_QUERY ()`


| Parameter | Description |
| --- | --- |
| num | The desired resolution x-axis value. |
| num | The desired resolution y-axis value. |


### Returns

XML: `<snapshot_query_string>url-query-string</snapshot_query_string> `