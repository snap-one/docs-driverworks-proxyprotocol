## PROPERTY\_DEFAULTS

Notification sent from the protocol driver through [ON DRIVER LATE INIT][1] containing the camera's default properties


### Signature

`PROPERTY_DEFAULTS ()`


| Parameter | Description |
| --- | --- |
| num | HTTP Port. Default port is 80. |
| num | RTSP Port. Default port is 554. |
| bool | `AUTHENTICATION_REQUIRED`  True/False. |
| str | `AUTHENTICATION_TYPE`  “BASIC” or “DIGEST”. |
| str | Username - `deafult_username` |
| str | Password - `deafult_password` |


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-api/#miscellaneous-interface-ondriverlateinit