## SINGLE SETPOINT CHANGED

Used to inform the proxy that the single setpoint has changed. This notification changes variables `SINGLE_SETPOINT_F` and `SINGLE_SETPOINT_C`. It fires the event `Single Setpoint Changed`.


 
### Signature

`SINGLE_SETPOINT_CHANGED ()` 


| Parameter | Description |
| --- | --- |
| int | SETPOINT: he new temperature setpoint value. |
| str | SCALE: The scale being used for the setpoint. The values allowed are CELSIUS, C, FAHRENHEIT, or F |
 

### Returns

`None`


