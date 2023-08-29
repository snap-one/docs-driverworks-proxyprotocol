## ACCEPT\_CALL

The ACCEPT\_CALL command is sent from the Intercom Proxy to the device driver. When the driver receives the ACCEPT\_CALL command, it must handle the command in a manner that enables the device to accept the incoming call. When implemented successfully, receipt of the ACCEPT\_CALL command is followed the [CALL\_ACCEPTED][1] notification being sent from the device driver to the Proxy.


### Signature

`ACCEPT_CALL ()`


Call Flow:

1. A SIP invite to a call is received by the device via the device driver and the device enters a ringing state.
2. The device goes into a state of “incoming call”. 
3. This needs to trigger an Incoming\_Call notification which is sent from the device, via the device driver, to the Proxy.
4. Upon call acceptance, this is followed by the device driver sending a CALL\_ACCEPTED notification to the Proxy.


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE` - The proxy ID of the callee |
| num|  `SESSION_ID` -  The session ID of the call. Session ID is established when a call is initiated and serves as a unique identifier of the call. |
| num | AUDIO - The requested audio cap for the call: 0 = Full Duplex, 1 = Transmit Only, 2 = Receive Only, 3 = Inactive| |
| num | VIDEO - The requested video cap for the call. 0 = Full Duplex, 1 = Transmit Only, 2 = Receive Only. The Audio channel cannot be Inactive.|


### Returns

`None`


### Usage Notes:
This call command can be initiated by pressing a button on a UI displayed on devices running Navigator, Control-Control in ComposerPro and Composer Programming.


[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-call_accepted