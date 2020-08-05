## START BROADCAST CALL

This command is issued by the initiator of a new broadcast call to a pre-defined group of intercom devices.  The command will result in an `OUTGOING_CALL` notification to the initiator and an `INCOMING_CALL` notification to the receiver.  


### Signature

`START_BROADCAST_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | AUDIO - The requested audio cap for the call. |
| num | VIDEO - The requested video cap for the call. |
| num|  `GROUP_ID` - The group ID of the group being called |


### Returns

`None`
