## REJECT\_CALL

This command may be issued by the receiver of a call invitation and causes the call associated with the given session id to be rejected (ended).  This command will result in a `CALL_REJECTED` notification being sent to both the initiator and the receiver of the call.


### Signature

`REJECT_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` - The session ID of the call |


### Returns

`None`

