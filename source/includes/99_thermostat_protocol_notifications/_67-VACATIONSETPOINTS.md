## VACATION\_SETPOINTS

Notification that should be sent to the proxy when setpoints have been changed for vacation mode. This Notification is not to be used with Preset Scheduling. The capability  `has_vacation_mode` must be set to true for the vacation commands and notifications to be executed. 


### Name

`VACATION_ SETPOINTS ()` 


| Parameter          | Type | Description                                                      |
| ------------------ | ---- | ---------------------------------------------------------------- |
| VAC HEAT SETPOINT  | NUM  | New temperature for the heating setpoint while in vacation mode. |
| VAC COOL SETPOINT: | NUM  | New temperature for the cooling setpoint while in vacation mode. |
| UNITS              | STR  | F or C – Fahrenheit or Celsius.                                  |


### Returns

`None`

