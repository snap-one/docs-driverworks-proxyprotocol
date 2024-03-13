## ONLINE\_CHANGED

Used to inform the proxy that the online status of the device has changed.  Due to backwards compatibility, the proxy starts 'online' as many old devices did not report online status.  UI functionality will be disabled if the light is offline.

### Name

`ONLINE_CHANGED ()`



| Parameter | Type  | Description                                      |
| --------- | ----- | ------------------------------------------------ |
| STATE     | BOOL. | True/False. Whether the device is online or not. |


### Returns

`None`