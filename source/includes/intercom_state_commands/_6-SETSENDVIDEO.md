## SET SEND VIDEO

This command is issued by a proxy consumer to cause the state of the send video setting to change.  This command will result in a `SEND_VIDEO_CHANGED`


### Signature

`C4: SET_SEND_VIDEO ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```
<SET_SEND_VIDEO>
   <sendVideo>[1]</sendVideo>
</SET_SEND_VIDEO>
```
