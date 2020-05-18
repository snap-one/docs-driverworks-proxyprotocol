## SET RINGER VOLUME

This command is issued to cause the ringer volume setting to be changed for the indicated intercom device.  This command will result in a `RINGER_VOLUME_CHANGED` notification to the proxy consumer for the indicated intercom device.


### Signature

`C4: SET_RINGER_VOLUME E ()`


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
