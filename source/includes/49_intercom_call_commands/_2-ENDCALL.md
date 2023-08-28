## END\_CALL

This command only applies to an established call session. If a call has not been established – it cannot be ended. The END\_CALL command is sent from the Intercom Proxy to the device driver when an established call is to be terminated. After the call is terminated, the device driver must send the CALL\_ENDED notification to both the initiator and the receiver of the call.  


### Signature

`END_CALL ()`


Call Flow:
1. A SIP invite to a call is received by the device via the device driver and the device enters a ringing state.
2. The device goes into a state of “incoming call”. 
3. This needs to trigger an Incoming\_Call notification which is sent from the device, via the device driver, to the Proxy.
4. Upon call acceptance, this is followed by the device driver sending a CALL\_ACCEPTED notification to the Proxy.
5. When the call is to be terminated, The END\_CALL command is sent from the intercom proxy to the device driver.
6. When the device driver terminates the call (SIP BYE), the CALL\_ENDED notification is sent from the driver to the Intercom proxy.


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller.|
| num | `REMOTE_DEVICE` - The proxy ID of the callee. |
| str |  `SESSION_ID` - The session ID of the call. Session ID is established when a call is initiated and serves as a unique identifier of the call. |


### Returns

`None`
