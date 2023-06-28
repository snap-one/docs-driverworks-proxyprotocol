## ACCEPT\_CALL

This command is used to programmatically accept a ringing call on a device. 
It may be issued by the receiver of a call invitation (i.e. an [`INCOMING_CALL notification`][1]) and causes the call associated with the given session id to be accepted. This command will result in a [`CALL_ACCEPTED`][2] notification being sent to both the initiator and the receiver of the call.


### Signature

`ACCEPT_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` -  The session ID of the call. Session ID is established when a call is initiated and serves as a unique identifier of the call. |
| num | AUDIO - The requested audio cap for the call. |
| num | VIDEO - The requested video cap for the call. |


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#incoming-call
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#call-accepted