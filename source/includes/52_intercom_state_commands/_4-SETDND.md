## SET DND 

This command is issued to toggle the “Do Not Disturb” setting of the intercom. This command will result in a `DND_CHANGED` notification to the proxy.


### Signature

`C4: SET_DND ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```
<SET_DND>
   <dndSettingd>[true]</dndSetting>
</SET_DND>
```
