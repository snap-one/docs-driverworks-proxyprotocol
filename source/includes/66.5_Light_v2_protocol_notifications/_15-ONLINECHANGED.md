## ONLINE CHANGED

Used to inform the proxy that the online status of the device has changed.  Due to backwards compatibility, the proxy starts 'online' as many old devices did not report online status.  UI functionality will be disabled if the light is offline.

### Signature

`ONLINE_CHANGED ()`



| Parameter | Description |
| --- | --- |
| bool | STATE: True/False. Whether the device is online or not. |


### Returns

`None`