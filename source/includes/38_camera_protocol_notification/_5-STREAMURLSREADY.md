## STREAM URLS READY

Notify used for following up to a GET\_STREAM\_URLS Synchronous call.  This Notify will let a UI know that the URL information they requested is ready.  The driver must use the same key parameter value that was returned to the UI as the key parameter in this notify.



### Signature

`STREAM_URLS_READY ()`


| Parameter | Description |
| --- | --- |
| key | Key of the originating call for the snapshot to be created. |
| str | String of XML object as described in the description of this call. |


### Returns

`None`


### Examples


```lua
<streams key="1234">
<stream url="http://192.168.1.150/view_camera.cgi">
</streams>

--- or

<streams key="1234" camera_address="192.168.1.150">
<stream url="https://192.168.1.150:443/view_camera.cgi" codec=mjpeg>
<stream url="http://192.168.1.150:80/view_camera_h265.cgi" codec=h265>
</streams>

--- A more feature rich camera could also provide more options to allow clients to pick a better stream:

<streams key="1234" camera_address="server.company.com">
<stream url="rtsps://192.168.1.150:554/rtsp.cgi" codec="h265" resolution"1920x1080" fps="60">
<stream url="rtsps://192.168.1.150:554/cloudapi.cgi?fh2f5hw2" codec="h265" resolution"640x480" fps="5">
<stream url="rtsp://192.168.1.150:554/cloudapi.cgi?fh2f4hw1" codec="h264" resolution"1920x1080" fps="60">
<stream url="rtsp://192.168.1.150:554/cloudapi.cgi?fh2f4hw2" codec="h264" resolution"640x480" fps="5">
<stream url="https://192.168.1.150:443/cloudapi.cgi?fh2fhsw3" codec="mjpeg" resolution"1920x1080" fps="20">
<stream url="https://192.168.1.150:443/cloudapi.cgi?fh2fhsw5" codec="mjpeg">
<stream url="http://192.168.1.150:80/cloudapi.cgi?fh2fhw3" codec="mjpeg" resolution"1920x1080" fps="20">
<stream url="http://192.168.1.150:80/cloudapi.cgi?fh2fhw5" codec="mjpeg">
</streams>
```
