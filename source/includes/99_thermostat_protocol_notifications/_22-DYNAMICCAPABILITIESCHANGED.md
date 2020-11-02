## DYNAMIC CAPABILITIES CHANGED TSTAT

Dynamic Capabilities is a way for a protocol driver to send updates about some capabilities that can be changed when settings change on the hardware.  An example would be a thermostat that has a humidifier added would need to tell the proxy it can now do humidification as well as what the min, max and resolution of changes are for the setpoint. 

### Signature

`DYNAMIC_CAPABILITIES_CHANGED ()`


| Parameter | Description |
| --- | --- |
| bool | `HAS_OUTDOOR_TEMPERATURE`: boolean to enable/disable \`hasoutdoortemperature capability, if the device supports this feature, default is false. |
`| bool |`CAN\_CHANGE\_SCALE\`: boolean to enable/disable Navigators UI's and composer from being able to change the scale of the hardware. |
| bool | `HAS_HUMIDITY`: boolean to enable/disable \`\`[`has_humidity`][1] capability, if the device supports this feature, default is false |
| bool | `HAS_SINGLE_SETPOINT`: Boolean used to turn single setpoint mode to on or off. Defaults to false (off). |
| int | `HUMIDIFY_SETPOINT_MIN`: Minimum Setpoint, int 0-100 that will do the same thing as the [`setpoint_humidify_min`][2] capability, default 0 |
| int | `HUMIDIFY_SETPOINT_MAX`: Minimum Setpoint, int 0-100 that will do the same thing as the [`setpoint_humidify_max`][3] capability, default 100 |
| int | `HUMIDIFY_SETPOINT_RESOLUTION`:  What increment to use (ie 1,3,5,10,etc), will do the same thing as the `setpoint_humidify_resolution` capability, default 1 |
| int | `HUMIDITY_SETPOINT_DEADBAND`: What the deadband between humidify and dehumidify is, will do the same thing as the `setpoint_humidity_deadband` capability, default 10 |
| int | `DEHUMIDIFY_SETPOINT_MIN`: Minimum Setpoint, int 0-100 that will do the same thing as the `setpoint_dehumidify_min` capability, default 0 |
| int | `DEHUMIDIFY_SETPOINT_MAX`: Minimum Setpoint, int 0-100 that will do the same thing as the `setpoint_dehumidify_max` capability, default 100 |
| int | `DEHUMIDIFY_SETPOINT_RESOLUTION`: What increment to use (ie 1,3,5,10,etc), will do the same thing as the `setpoint_dehumidify_resolution` capability, default 1 |


### Returns

`None`


[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#thermostat-capabilities
[2]:	https://control4.github.io/docs-driverworks-proxyprotocol/#thermostat-capabilities
[3]:	https://control4.github.io/docs-driverworks-proxyprotocol/#thermostat-capabilities