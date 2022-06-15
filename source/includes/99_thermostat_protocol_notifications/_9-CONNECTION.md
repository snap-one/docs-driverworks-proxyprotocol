## CONNECTION

Boolean to enable/disable [`can_dehumidify`][1] capability. If the device supports this feature, default is False.


### Signature

`CONNECTION ()`


| Parameter | Description |
| --- | --- |
| bool | CONNECTED: true/false. |
| DataToUI name | If  `is_connected` and is a boolean value. If `IS_CONNECTED` is false, the UI will show "–" where the temperature would be, indicating the device is off line. Also, sending a false will prevent any of the Control Buttons from appearing on the UI. |



### Returns

`None`



[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#thermostat-capabilities