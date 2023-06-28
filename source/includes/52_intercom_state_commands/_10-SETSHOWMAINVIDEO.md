## SET\_SHOW\_MAIN\_VIDEO

This command is issued to cause the ringer volume setting to be changed for the indicated intercom device.  This command will result in a [`RINGER_VOLUME_CHANGED`][1] notification to the proxy consumer for the indicated intercom device.


### Signature

`SET_SHOW_MAIN_VIDEO ()`


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

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#ringer-volume-changed