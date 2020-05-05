## END CALL

This command can be issued by either the initiator or receiver and causes the indicated session to be ended.  This command will result in a `CALL_ENDED` notification being sent to both the initiator and the receiver of the call.  For broadcast calls, when the caller ends the call the remoteAor should be set to the value “broadcast” (without the quotes)


### Signature

`C4:END_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` - The session ID of the call |


### Returns

`None`
