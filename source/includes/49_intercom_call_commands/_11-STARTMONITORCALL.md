## START\_MONITOR\_CALL

The START\_MONITOR\_CALL command is sent from the Intercom Proxy to the device driver. When the driver receives the START\_MONITOR\_CALL command, it must be in monitor mode to successfully handle it. A device can be set to monitor mode via Composer Pro or Navigator. When implemented successfully, the command will result in an [INCOMING\_CALL][1] notification being sent to the proxy. Note that in addition to a device being in monitor mode, it should also mute itself or turn volume level to zero when receiving the START\_MONITOR\_CALL. This ensures that no sounds come from the receiving device. This is useful in the case where a device is being used as a baby monitor.


### Signature

`START_MONITOR_CALL ()`


Call Flow:

1. START\_MONITOR\_CALL command is sent from the intercom proxy to the device driver.
2. A SIP invite to a call is received by the device via the device driver and the device enters a ringing state.
3. The device goes into a state of “incoming call”. 
4. This needs to trigger an Incoming\_Call notification which is sent from the device, via the device driver, to the Proxy.
5. Because the device receiving the call is in monitor mode, the call is automatically accepted.
6. Upon call acceptance, this is followed by the device driver sending a [CALL\_ACCEPTED][2] notification to the Proxy.





| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE_ID` - The proxy ID of the callee |
| num | AUDIO - The requested video capacity for the call. 0 = Full Duplex (SEND\_RECV), 1 = Transmit Only (SEND\_ONLY), 2 = Receive Only RECV\_ONLY), 3 = Inactive (NO\_SEND\_RECV)  |
| num | VIDEO - The requested video capacity for the call. 0 = Full Duplex (SEND\_RECV), 1 = Transmit Only (SEND\_ONLY), 2 = Receive Only RECV\_ONLY). The Audio channel cannot be Inactive.|
| num | RING - The ring parameter for the call 0 = default Navigator beep,  1 = doorbell chime. Note that the RING param must be passed for the function to work correctly. The driver must place the receiving on mute or turn volume level to zero |


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-incoming_call
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-call_accepted