## START\_CALL

The START\_CALL command is initiated through Programming or Control/Control in ComposerPro. It is sent to the Intercom Proxy, which then sends a START\_CALL to the device driver. When the driver receives the START\_CALL command, it must handle the command in a manner that enables the device to begin a call. When implemented successfully, receipt of the START\_CALL command is followed by the [CALL\_ACCEPTED][1] notification being sent from the device driver to the Proxy.


### Signature

`START_CALL ()`


Call Flow:

1. Upon receiving a START\_CALL command from the Proxy, a SIP invite is generated.
2. The SIP invite to a call is received by the device via the device driver and the device enters a ringing state.
3. The device goes into a state of “outgoing call”. 
4. This needs to trigger an [Outgoing\_Call][2] notification which is sent from the device, via the device driver, to the Proxy.
5. Upon call acceptance, this is followed by the device driver that receives the call, sending a CALL\_ACCEPTED notification to the Proxy.


| Parameter | Description                                                                                                                                                                                |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| num       | `DEVICE_ID` - The proxy ID of the caller                                                                                                                                                   |
| num       | `REMOTE_DEVICE_ID` - The proxy ID of the callee                                                                                                                                            |
| num       | AUDIO - The requested video capacity for the call. 0 = Full Duplex (SEND\\\_RECV), 1 = Transmit Only (SEND\\\_ONLY), 2 = Receive Only RECV\\\_ONLY), 3 = Inactive (NO\\\_SEND\\\_RECV)     |
| num       | VIDEO - The requested video capacity for the call. 0 = Full Duplex (SEND\\\_RECV), 1 = Transmit Only (SEND\\\_ONLY), 2 = Receive Only RECV\\\_ONLY). The Audio channel cannot be Inactive. |
| num       | RING - The ring parameter for the call 0 = plays default Navigator beep, 1 = plays doorbell chime                                                                                          |


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-call_accepted
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-outgoing_call