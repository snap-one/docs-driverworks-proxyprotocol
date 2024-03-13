## SINGLE\_SETPOINT\_CHANGED

Used to inform the proxy that the single setpoint has changed. This notification changes variables `SINGLE_SETPOINT_F` and `SINGLE_SETPOINT_C`. It fires the event `Single Setpoint Changed`.



### Name

`SINGLE_SETPOINT_CHANGED ()` 


| Parameter | Type | Description                                                                                |
| --------- | ---- | ------------------------------------------------------------------------------------------ |
| SETPOINT  | INT  | The new temperature setpoint value.                                                        |
| SCALE     | STR  | The scale being used for the setpoint. The values allowed are CELSIUS, C, FAHRENHEIT, or F |

 

### Returns

`None`


