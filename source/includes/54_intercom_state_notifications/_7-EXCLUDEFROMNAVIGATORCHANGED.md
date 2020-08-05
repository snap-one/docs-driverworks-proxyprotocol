## EXCLUDE FROM NAVIGATOR CHANGED

This notification is issued by the proxy when the endpoint’s Exclude from Navigator setting has changed. 


### Signature

`EXCLUDE_FROM_NAVIGATOR_CHANGED ()`


| Parameter | Description |
| --- | --- |
| int | The proxy device id of the intercom endpoint whose device state information is being returned |
| int | dndSetting: Boolean flag indicating the current state for this setting. (0=false, 1=true) |


### Example

```lua
<device_state proxyid =[10]>
    <excludeFromNav>[0]</excludeFromNav>
</device_state>
```
