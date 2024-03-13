## GET\_MJPEG\_QUERY

Command that is initiated in Composer Pro and immediately returns a block of XML information. It returns the query string needed to create the URL for MJPEG server push request.


### Name

`GET_MJPEG_QUERY ()`


| Parameter | Description                                     |
| --------- | ----------------------------------------------- |
| num       | The desired resolution x-axis value.            |
| num       | The desired resolution y-axis value.            |
| num       | The delay in milliseconds between pushed frames |
| str       | Query. The path/query of the URL.               |


### Returns

XML: `<mjpeg_query_string> url-query-string</mjpeg_query_string>`