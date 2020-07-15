## SET CUSTOM SETTINGS

This command results in the Protocol Notification [`CUSTOM_SETTINGS`][1] being sent from the Protocol to the Proxy.


### Signature

`C4:SET_CUSTUM_SETTINGS ()`


| Parameter | Description |
| --- | --- |
| str | NAME: Required. |
| str | VALUE: Required. Value type must be converted based on custom setting type. |


### Returns

`None`



[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#custom-settings