## SET AUTO ANSWER

This command is issued to toggle the “Do Not Disturb” setting of the intercom. This command will result in an `AUTO_ANSWER_CHANGED` notification to the indicated proxy consumer.


### Signature

`C4: SET_AUTO_ANSWER ()`


| Parameter | Description |
| --- | --- |
| int | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`

### Example

```lua
<SET_AUTO_ANSWER>
   <autoAnswer>[0]</autoAnswer>
</SET_AUTO_ANSWER>
```
