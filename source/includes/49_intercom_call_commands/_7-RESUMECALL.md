## RESUME CALL

This command can be issued by an intercom device that has already paused the call associated with the indicated session id. This command will result in a `CALL_RESUMED` notification being sent to both the initiator and the receiver of the call.


### Signature

`C4:RESUME_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` - The session ID of the call |


### Returns

`None`

