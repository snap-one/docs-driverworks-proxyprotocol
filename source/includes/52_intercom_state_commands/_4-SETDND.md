## SET DND

This command is issued to toggle the “Do Not Disturb” setting of the intercom. 

### Signature

`C4: SET_DND ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<SET_DND>
   <dndSettingd>[true]</dndSetting>
</SET_DND>
```
