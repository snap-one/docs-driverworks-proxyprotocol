## PRESET\_DELETE

Adds a new Preset Schedule Preset (If protocol driver has the `can_preset_schedule` capability)



### Name

`PRESET_DELETE ()`


| Parameter     | Type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------- | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NAME          | STR  | Preset Name. Required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PRESET FIELDS | XML  | If a UI or Driver sends a bound call with a string that has invalid XML syntax, this field will be set to `<preset_field/>` and an error message will be logged to director.log when this occurs. Note that only a driver OR UI should specify the` _f or c. ` For example: `heat_setpoint_f`, `cool_setpoint_f`, `heat_setpoint_c`, `cool_setpoint_c` but not both. The proxy will auto insert the missing` _f or _c `based on the scales resolution if it detects one side is not supplied. This makes it so UI's and drivers do not need to calculate the correct value for the scale.  However, if a driver or UI does want to calculate it, the proxy will leave the value alone. In the same manner the proxy will not correct or anything if the` _f and _c `do not resolve to the equivalent temperature. |


### Returns

`None`


