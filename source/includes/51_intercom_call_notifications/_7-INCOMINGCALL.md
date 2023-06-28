## INCOMING\_CALL

This notification is issued when a call invite is received; it is only sent to the receiver involved in the specified session.


### Signature

`INCOMING_CALL ()`


| Parameter | Description |
| --- | --- |
| num | The Device ID of the Proxy. |
| num | The Session ID of the SIP session. |
| num | Call type. |
| num | `remote_device_id` = the proxy ID of the remote endpoint |
| num | value of the audio cap |
| num | value of the video cap |
