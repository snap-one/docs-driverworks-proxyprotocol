## DEC\_SETPOINT\_HEAT

Used to decrease the heat set point by 1. This command is handled by the proxy, and ends up creating a `SET_SETPOINT_HEAT` command to send to the protocol driver, unless the capability `can_inc_dec_setpoints` is set to true


### Name

`DEC_SETPOINT_HEAT ()`


### Parameter

`None`


### Returns

`None`

