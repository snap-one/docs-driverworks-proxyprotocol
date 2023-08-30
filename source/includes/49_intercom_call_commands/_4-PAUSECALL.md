## PAUSE\_CALL

**NOTE:** The PAUSE\_CALL command is currently deprecated and not available for use.\_ 
This command can be issued by either the initiator or receiver and causes the call associated with the indicated session to be placed on hold (or paused).  This command will result in a `CALL_PAUSED` notification being sent to both the initiator and the receiver of the call.


### Signature

`PAUSE_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` - The session ID of the call. Session ID is established when a call is initiated and serves as a unique identifier of the call. |


### Returns

`None`

