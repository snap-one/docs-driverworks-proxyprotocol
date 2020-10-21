## SNAPSHOT URLS READY

Notify used for following up to a GET_SNAPSHOT_URLS Synchronous call.  This Notify will let a UI know that the URL information they requested is ready.  The driver must use the same key parameter value that was returned to the UI as the key parameter in this notify.


### Signature

`SNAPSHOT_URLS_READY ()`


| Parameter | Description |
| --- | --- |
| key | Key of the originating call for the snapshot to be created. |
| str | String of XML object as described in the description of this call. |


### Returns

`None`


### Examples


```lua
<snapshots key="1234">
<snapshot url="http://192.168.1.150/view_camera.cgi">
</snapshots>

— or

<snapshots key="1234">
<snapshot url="http://192.168.1.150:80/custom_resolution_as_requested_by_client.cgi" resolution="644x481">
<snapshot url="https://192.168.1.150:443/view_snapshot.cgi" resolution="3840x2160">
<snapshot url="https://192.168.1.150:443/view_snapshot.cgi" resolution="1920x1080">
<snapshot url="https://192.168.1.150:80/view_snapshot.cgi" resolution="640x480">
</snapshots>
```
