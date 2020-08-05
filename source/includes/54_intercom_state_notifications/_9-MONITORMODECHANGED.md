## MONITOR MODE CHANGED

This notification is issued by the proxy when the endpoint’s Monitor Mode setting has changed. 


### Signature

`MONITOR_MODE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| int | The proxy device id of the intercom endpoint whose device state information is being returned |
| monitorMode | Boolean flag indicating the current value of this setting. (0=false, 1=true) |


### Example

```lua
<device_state proxyid =[10]>
    <monitorMode>[0]</monitorMode>
</device_state>
```

