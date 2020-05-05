## PAUSE CALL

This command can be issued by either the initiator or receiver and causes the call associated with the indicated session to be placed on hold (or paused).  This command will result in a `CALL_PAUSED` notification being sent to both the initiator and the receiver of the call.


### Signature

`C4:PAUSE_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` - The session ID of the call |


### Returns

`None`

