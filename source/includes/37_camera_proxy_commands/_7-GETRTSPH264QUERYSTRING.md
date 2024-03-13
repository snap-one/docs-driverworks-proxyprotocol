## GET\_ RTSP\_H264\_QUERY\_ STRING

Command that is initiated in Composer Pro and immediately returns a block of XML information. It returns the query string needed to create the URL for RTSP H264 stream request.


### Name

`GET_RTSP_H264_QUERY ()`


| Parameter | Description                                     |
| --------- | ----------------------------------------------- |
| num       | The desired resolution x-axis value.            |
| num       | The desired resolution y-axis value.            |
| num       | The delay in milliseconds between pushed frames |
| str       | Query. The path/query of the URL.               |


### Returns

XML: `<rtsp_h264_query_string> url-query-string</rtsp_h264_query_string>`