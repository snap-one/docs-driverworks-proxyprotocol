## STOPPED

State Notification used by the protocol to inform the proxy the blinds have stopped moving.  A Stop notification that uses the optional LEVEL parameter should be used if a blind is moving and changes direction.

### Signature

`C4:STOPPED ()`


| Parameter | Description |
| --- | --- |
| INT | LEVEL - Where the blinds stopped at. This will also set the general level as well to this value. |


### Returns

`None`


### Usage Note

This Notification Fires Director Event: Stop
`level_final` is also updated to the value passed in through the level parameter.
Sends DataToUI "Stopped" including: `level` - The level it stopped at.