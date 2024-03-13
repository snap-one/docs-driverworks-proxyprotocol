## PROPERTY\_DEFAULTS

Notification sent from the protocol driver through [ON DRIVER LATE INIT][1] containing the camera's default properties


### Name

`PROPERTY_DEFAULTS ()`


| Parameter                 | Type | Description                                 |
| ------------------------- | ---- | ------------------------------------------- |
| HTTP Port.                | NUM  | HTTP Port. Default port is 80.              |
| RTSP Port                 | NUM  | RTSP Port. Default port is 554.             |
| `AUTHENTICATION_REQUIRED` | BOOL | `AUTHENTICATION_REQUIRED`  True/False.      |
| `AUTHENTICATION_TYPE`     | STR  | `AUTHENTICATION_TYPE`  “BASIC” or “DIGEST”. |
| `deafult_username`        | STR  | Username - `deafult_username`               |
| `deafult_password`        | STR  | Password - `deafult_password`               |


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-api/#miscellaneous-interface-ondriverlateinit