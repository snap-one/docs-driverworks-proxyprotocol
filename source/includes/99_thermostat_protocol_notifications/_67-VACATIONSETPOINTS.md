## VACATION SETPOINTS

Notification that should be sent to the proxy when setpoints have been changed for vacation mode. This Notification is not to be used with Preset Scheduling. The capability  `has_vacation_mode` must be set to true for the vacation commands and notifications to be executed. 



### Signature

`VACATION_ SETPOINTS ()` 


| Parameter | Description |
| --- | --- |
| num | VAC HEAT SETPOINT: New temperature for the heating setpoint while in vacation mode. |
| num |VAC COOL SETPOINT: New temperature for the cooling setpoint while in vacation mode. |
| str | UNITS: F or C – Fahrenheit or Celsius. |


### Returns

`None`

