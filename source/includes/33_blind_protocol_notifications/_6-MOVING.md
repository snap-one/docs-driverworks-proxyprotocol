## MOVING

State Notification Used by the protocol to inform the proxy the blinds have started to move.

### Name

`MOVING ()`


| Parameter    | Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LEVEL TARGET | INT  | Integer of the target level that the blinds are currently expected to stop at.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| RAMP RATE    | NUM  | Number of milliseconds it is expected to take to get to the `level_target`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| LEVEL        | INT  | Optional. Integer of the level the blind started moving from. If not specified, the proxy assumes the last level sent by a [STOPPED][1] Notification. This optional parameter should be sent in the case the blind was moving to a level but is interrupted/commanded to go to a different level.  Without specifying this parameter in an interruption case, Toggle on UIs and UI display of blind movement and direction will be inaccurate. Drivers might need to do a STOP or GET for hardware position before the blind direction is commanded to go to the new position in order to obtain an accurate LEVEL for this value of where the blind was before the new movement began. |


### Returns

`None`


### Usage Note

This Notification Fires Director Event: Moving. Sends DataToUI:  "Moving" including:

- `level` - Where the blind is starting from.
- `level_target` - Where the blind is going to.
- `ramp_rate` - The number of milliseconds it will take the blind to reach this position.

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#blind-protocol-notifications-stopped