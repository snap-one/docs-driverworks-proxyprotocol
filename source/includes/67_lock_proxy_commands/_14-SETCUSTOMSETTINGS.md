## SET\_CUSTOM\_SETTINGS

This command results in the Protocol Notification [`CUSTOM_SETTINGS`][1] being sent from the Protocol to the Proxy.


### Name

`SET_CUSTOM_SETTINGS ()`


| Parameter | Type | Description                                                          |
| --------- | ---- | -------------------------------------------------------------------- |
| NAME      | STR  | Required.                                                            |
| VALUE     | STR  | Required. Value type must be converted based on custom setting type. |


### Returns

`None`



[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#lock-protocol-notifications-custom_settings