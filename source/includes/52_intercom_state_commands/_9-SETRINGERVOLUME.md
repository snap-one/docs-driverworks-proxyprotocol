## SET\_RINGER\_VOLUME

This command is issued to cause the ringer volume setting to be changed for the indicated intercom device.  This command will result in a [`RINGER_VOLUME_CHANGED`][1] notification to the proxy consumer for the indicated intercom device.


### Signature

`SET_RINGER_VOLUME ()`


| Parameter | Description |
| --- | --- |
| NUM | A numeric value 0 - 100  indicating the new value for the ringer volume setting |


### Returns

`None`


### Example

```lua
<SET_RINGER_VOLUME>
   <ringerVol>[1]</ringerVol>
</SET_RINGER_VOLUME>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#ringer-volume-changed