## START  MONITOR CALL

This command is issued by the initiator of a new monitoring call to a specified receiver.  The receiver must be in monitor mode.  The command will result in an `OUTGOING_CALL` notification to the initiator and an `INCOMING_CALL` notification to the receiver


### Signature

`START_MONITOR_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE_ID` - The proxy ID of the callee |
| num | AUDIO - The requested audio cap for the call. |
| num | VIDEO - The requested video cap for the call. |
| num|  RING - The ring parameter for the call |


### Returns

`None`
