## SEND VIDEO CHANGED

This notification is issued by the proxy when the endpoint’s Monitor Mode setting has changed. 


### Signature

`SEND_VIDEO_CHANGED ()`


| Parameter | Description |
| --- | --- |
| int | The proxy device id of the intercom endpoint whose device state information is being returned |
| BOOL | sendVideo: Boolean flag indicating the current state for this setting. (0=false, 1=true) |


### Example

```lua
<device_state proxyid =[10]>
    <sendVideo>[0]</sendVideo>
</device_state>
```

