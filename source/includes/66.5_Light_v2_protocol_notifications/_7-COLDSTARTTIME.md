## COLDSTARTTIME

Used to inform the proxy that the hardware Cold Start level has changed.  This is useful for hardware such as Control4’s Gen3 lighting where the hardware supports temporarily setting the brightness to a level for this number of milliseconds in order to 'jump start' the capacitors/ballasts on LED and florescent lights.  This value changes over time as capacitors and ballasts age.

### Signature

`C4:COLD_START_TIME ()`


| Parameter | Description |
| --- | --- |
| int | BRIGHTNESS: Number of milliseconds that the light is turned on to the COLD_START_LEVEL value. |


### Returns

`None`