## CALL\_ENDED

The CALL\_ENDED notification is generated by the device driver and sent to the intercom proxy when a call session is ended. After a SIP call is ended, any device participating in the call should send CALL\_ENDED notification.


### Signature

`CALL_ENDED ()`


| Parameter | Description |
| --- | --- |
| num | The Device ID of the Proxy. |
| str | The Session ID of the SIP session. Session ID is established when a call is initiated and serves as a unique identifier of the call. |
| num | Hang up type: 0 = LOCAL, 1 = REMOTE, 2 = BCASTEMPTY, 3 = NOTFOUND, 4 = DEVBUSY, 5 = NOANSWER, 6 = HUNKOWN |  


### Usage Notes:
The CALL\_ENDED notification is only applicable to devices that are active in an answered, call session. For example, in the case of a group call, the CALL\_ENDED notify is sent only by the device that was participating in the call. Other devices in the call list should sent a [CALL\_REJECTED][1] to the proxy. 




[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-call_rejected