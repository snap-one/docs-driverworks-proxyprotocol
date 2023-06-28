## END\_CALL

Used by Programming or ComposerPro. Terminates the current call. A full session (completed call) must have occurred in order for End Call to work. End Call is not applicable to calls that are in a ringing state. Upon executing End Call both ends of the call are terminated.

This command can be issued by either the initiator or receiver and causes the indicated session to be ended.  This command will result in a `CALL_ENDED` notification being sent to both the initiator and the receiver of the call.  For broadcast calls, when the caller ends the call the remoteAor should be set to the value “broadcast” (without the quotes)


### Signature

`END_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num |  `SESSION_ID` - The session ID of the call. Session ID is established when a call is initiated and serves as a unique identifier of the call. |


### Returns

`None`
