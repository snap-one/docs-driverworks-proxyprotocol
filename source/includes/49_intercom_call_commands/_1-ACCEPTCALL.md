## ACCEPT CALL

This command may be issued by the receiver of a call invitation (i.e. an [`INCOMING_CALL notification`][1]) and causes the call associated with the given session id to be accepted. This command will result in a [`CALL_ACCEPTED`][2] notification being sent to both the initiator and the receiver of the call.


### Signature

`C4:ACCEPT_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` - The session ID of the call |
| num | AUDIO - The requested audio cap for the call. |
| num | VIDEO - The requested video cap for the call. |


### Returns

`None`

[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#incoming-call
[2]:	https://control4.github.io/docs-driverworks-proxyprotocol/#call-accepted