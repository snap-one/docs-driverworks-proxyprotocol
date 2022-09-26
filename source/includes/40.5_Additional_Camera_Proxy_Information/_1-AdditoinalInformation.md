

### Camera Streams

In conjunction with the release of O.S. 3.3.1, the Camera Proxy has been enhanced with regard to what types of streams it provides. This is a result of the release of Control4’s next generation T4 touchscreens, new controllers and support for H.265 streaming. Camera drivers now have the ability to provide more stream options and can support a larger set of mixed hardware environments.

Also, Navigators now support streaming tiles which results in the need to stream many cameras in parallel. To provide this functionality over a remote connection, it is desirable to offer the option to pick a lower bandwidth stream.


### Default Configured Streams for New Cameras

For the best experience, cameras should be minimally configured with the following streams by default:

| Next Gen C4 OSD | T4 Touch Screens | Mobile|
| --- | --- | --- |
|High Resolution H.265| 1080p H.265| High Resolution H.265|

| Legacy C4 OSD | T3 Touch Screens |
| --- | --- |
| 720p H.264| 720p H.264|

|Small Streaming Tiles|
| --- |
| Low Resolution H.265|


### Driver Support for Multiple Streams

Beginning with O.S. 3.3.1, new camera drivers should implement the new dynamic streams API to provide a list of streams that the  Navigators can pick from. In order to support dynamic streams the driver should:

1. Set the [requires\_dynamic\_stream\_urls][1] dynamic capability to “true”.

2. Implement the [GET\_STREAM\_URLS][2] UI request command. _See Related APIs below for more information._ This can be either implemented synchronously, by returning the list of cameras directly or it can also be implemented asynchronously. For example, if the driver needs to query a web service to get the current streams.

If implemented asynchronously, when the stream list is available it will be necessary to send the Proxy the [STREAM\_URLS\_READY][3] Notify with the results. 

Drivers that do not have static URLs for streams will need to respond to the GET\_STREAM\_URLS call with an XML object that indicates the URL(s) is/are being generated and include a key with the response.  Once the driver has been able to obtain a URL for the stream, the driver should send a STREAM\_URLS\_READY Notify with the same key that is provided with this Synchronous call response.  An example of the response is:

`<streams generating_key="1234"/>`

The key should be a unique 32 bit integer value.  We recommend starting at 1 and incrementing by 1 for each request that comes in.

Also, if the driver does have a valid temporary URL that is still valid when it gets the call, no further Notify is needed and the driver should respond to this call with the XML of streams information.

To indicate to a client that the driver supports this API call, a driver needs to set the requires\_dynamic\_stream\_urls capability to true in the driver c4i or via DYNAMIC\_CAPABILITIES\_CHANGED Notify.

If no Port is provided with a URL, the following ports are used by all clients as the default for the transport:

- http - 80
- https - 443
- rtsp - 554
- rtsps - 443


### Support for Caching  URLs

The ability to cache the streams list is also supported. This removes the need to have to execute the GET\_STREAM\_URLS request every time a camera stream is loaded. This is supported with a new capability added in O.s 3.3.1: [dynamic\_urls\_use\_type][4]. 

The driver also needs to send a DYNAMIC\_URLS\_CHANGED notification to the proxy when the configured URLs have been changed. The proxy would then send a "DYNAMIC\_URLS\_CHANGED" DataToUI in response to this that the Navigators would key off of to refresh any cached URLs. This is useful for driver's with MULTIPLE use type URLs.






[1]:	https://snap-one.github.io/docs-driverworks-proxy-protocol-3.3.1-beta/#requires_dynamic_stream_urls
[2]:	https://snap-one.github.io/docs-driverworks-proxy-protocol-3.3.1-beta/#get-stream-urls
[3]:	https://snap-one.github.io/docs-driverworks-proxy-protocol-3.3.1-beta/#stream_urls_ready
[4]:	https://snap-one.github.io/docs-driverworks-proxy-protocol-3.3.1-beta/#dynamic_urls_use_type