## SET\_CAN\_STOP

Configuration Notification used by the protocol to inform the proxy if the blind supports stopping or not.

### Name

`SET_CAN_STOP ()`


| Parameter      | Type | Description                                              |
| -------------- | ---- | -------------------------------------------------------- |
| SET\_CAN\_STOP | BOOL | A boolean indicating if the blind control supports stop. |


### Returns

`None`


### Usage Note
The blind level will be sent to the UI using a DataToUI as set `can_stop_click = boolean`. This Notification sends DataToUI of: `blind_setup xml`.