## DYNAMIC\_CAPABILITIES\_CHANGED TSTAT

Dynamic Capabilities is a way for a protocol driver to send updates about some capabilities that can be changed when settings change on the hardware.  An example would be a thermostat that has a humidifier added would need to tell the proxy it can now do humidification as well as what the min, max and resolution of changes are for the setpoint. 

### Name

`DYNAMIC_CAPABILITIES_CHANGED ()`


| Parameter                        | Type | Description                                                                                                                             |
| -------------------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `HAS_OUTDOOR_TEMPERATURE`        | BOOL | boolean to enable/disable `hasoutdoortemperature` capability, if the device supports this feature, default is false.                    |
| `CAN_CHANGE_SCALE`               | BOOL | boolean to enable/disable Navigators UI's and composer from being able to change the scale of the hardware.                             |
| `HAS_HUMIDITY`                   | BOOL | boolean to enable/disable [`has_humidity`][1] capability, if the device supports this feature, default is false                         |
| `HAS_SINGLE_SETPOINT`            | BOOL | Boolean used to turn single setpoint mode to on or off. Defaults to false (off).                                                        |
| `HUMIDIFY_SETPOINT_MIN`          | INT  | Minimum Setpoint, int 0-100 that will do the same thing as the [`setpoint_humidify_min`][2] capability, default 0                       |
| `HUMIDIFY_SETPOINT_MAX`          | INT  | Minimum Setpoint, int 0-100 that will do the same thing as the [`setpoint_humidify_max`][3] capability, default 100                     |
| `HUMIDIFY_SETPOINT_RESOLUTION`   | INT  | What increment to use (ie 1,3,5,10,etc), will do the same thing as the `setpoint_humidify_resolution` capability, default 1             |
| `HUMIDITY_SETPOINT_DEADBAND`     | INT  | What the deadband between humidify and dehumidify is, will do the same thing as the `setpoint_humidity_deadband` capability, default 10 |
| `DEHUMIDIFY_SETPOINT_MIN`:       | INT  | Minimum Setpoint, int 0-100 that will do the same thing as the `setpoint_dehumidify_min` capability, default 0                          |
| `DEHUMIDIFY_SETPOINT_MAX`        | INT  | Minimum Setpoint, int 0-100 that will do the same thing as the `setpoint_dehumidify_max` capability, default 100                        |
| `DEHUMIDIFY_SETPOINT_RESOLUTION` | INT  | What increment to use (ie 1,3,5,10,etc), will do the same thing as the `setpoint_dehumidify_resolution` capability, default 1           |


### Returns

`None`


[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#thermostat-capabilities
[2]:	hhttps://snap-one.github.io/docs-driverworks-proxyprotocol/#thermostat-capabilities
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#thermostat-capabilities