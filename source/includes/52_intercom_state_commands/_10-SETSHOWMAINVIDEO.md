## SET SHOW MAIN VIDEO

This command is issued to cause the ringer volume setting to be changed for the indicated intercom device.  This command will result in a `RINGER_VOLUME_CHANGED` notification to the proxy consumer for the indicated intercom device.


### Signature

`C4: SET_SHOW_MAIN_VIDEO ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new value for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<SET_SHOW_MAIN_VIDEO>
   <showMainVideo>[0]</showMainVideo>
</SET_SHOW_MAIN_VIDEO
```
