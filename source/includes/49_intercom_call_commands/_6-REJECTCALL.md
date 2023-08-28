## REJECT\_CALL

The REJECT\_CALL command is sent from the Intercom Proxy to the device driver. When the driver receives the Reject Call command, it must handle the command in a manner that enables the device to reject the incoming call. When implemented successfully, receipt of the REJECT\_CALL command should be followed by sending a [CALL\_REJECTED][1] notification from the device driver to the Proxy.


### Signature

`REJECT_CALL ()`


Call Flow:
1. A SIP invite to a call is received by the device via the device driver and the device enters a ringing state. 
2. The device goes into a state of “incoming call”. 
3. This needs to trigger an [Incoming\_Call][2] notification which is sent from the device, via the device driver, to the Proxy.
4. Upon call acceptance, this is followed by the device driver sending a [CALL\_REJECTED][3] notification to the Proxy.


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller. |
| num | `REMOTE_DEVICE` - The proxy ID of the callee. |
| str |  `SESSION_ID` - The session ID of the call. |


### Returns

`None`


### Usage Notes:

This command can be initiated by pressing a button on a UI displayed on devices running Navigator, Control-Control in ComposerPro and Composer Programming. 

The Reject Call command has no effect when sent during an active call session. End Call should be used in this instance.

If auto-answer is enabled, it overrides the option to reject the call and the Proxy will automatically accept it.

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-call_rejected
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-incoming_call
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-call_rejected