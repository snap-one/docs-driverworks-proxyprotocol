## MUTE\_CALL

This command only applies to an established call session. If a call has not been established – it cannot be muted. Likewise, a call cannot be muted when it is in a ringing state or a SIP BYE or ENDING states. The MUTE\_CALL command is sent from the Intercom Proxy to the device driver. When the driver receives the MUTE\_CALL command, it must handle the command in a manner that enables the device to place the existing call in a muted or un-muted state. Placing the device in a true muted state or setting the device volume to zero is supported for muting purposes. There is no associated notification for the MUTE\_CALL command. The device driver must maintain the state of the call in order to un-mute or mute the call correctly


### Signature

`MUTE_CALL ()`


Call Flow:
1. A SIP invite to a call is received by the device via the device driver and the device enters a ringing state.
2. The device goes into a state of “incoming call”. 
3. This needs to trigger an Incoming\_Call notification which is sent from the device, via the device driver, to the Proxy.
4. Upon call acceptance, this is followed by the device driver sending a CALL\_ACCEPTED notification to the Proxy.
5. When the call is to be muted or un-muted, the MUTE\_CALL command is sent from the intercom proxy to the device driver.


| Parameter | Description |
| --- | --- |
| bool |  muteAudio - A Boolean flag indicating whether to mute or un-mute the indicated session. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<MUTE_CALL>
   <muteAudio>[0]</muteAudio>
</MUTE_CALL>
```
