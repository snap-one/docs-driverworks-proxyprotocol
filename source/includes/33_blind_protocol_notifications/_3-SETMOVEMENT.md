## SET\_MOVEMENT

Configuration Notification used by the protocol to inform the proxy that the driver is a particular blind movement function.  If this is used, the proxy will disable the pull-down from being select-able by a dealer.

### Name

`SET_MOVEMENT ()`


| Parameter    | Type | Description                              |
| ------------ | ---- | ---------------------------------------- |
| SET MOVEMENT | INT  | Enumeration of the blind  movement type. |

Movement Types:

- 0 - Open/Close (Open/Close)
- 1 - Up to Down (Up is open, Down is closed)
- 2 - Down to Up (Down is open, Up is Closed)
- 3 - Out to In (Out is Open, In is Open)
- 4 - Left to Right (Left is Open, Right is Closed)
- 5 - Right to Left (Right is Open, Left is Closed)

If set to -1 then a dealer can again select a choice from a pull-down in the proxy property control.


### Returns

`None`


### Usage Note

 This Notification sends DataToUI of: `blind_setup xml`.