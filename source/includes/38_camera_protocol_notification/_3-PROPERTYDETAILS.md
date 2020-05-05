## PROPERTY DETAILS

Notification sent from the protocol driver through `ON_DRIVER_LATE_INIT` containing the camera's default properties


### Signature

`C4:PROPERTY_DETAILS ()`


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
