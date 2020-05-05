## OUTGOING CALL

This notification is issued when a call invite is SENT; it is only sent to the initiator involved in the specified session.


### Signature

`C4: OUTGOING_CALL ()`


| Parameter | Description |
| --- | --- |
| num | The Device ID of the Proxy. |
| num | The Session ID of the SIP session. |
| num | Call type. |
| num | `remote_device_id` = the proxy ID of the remote endpoint |
| num | value of the audio cap |
| num | value of the video cap |