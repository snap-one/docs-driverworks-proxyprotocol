## AIR\_TEMP\_CHANGED

Sent to the proxy to indicate that the air temperature has changed


### Signature

`AIR_TEMP_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `TEMPERATURE` | Temperature value. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "AIR_TEMP_CHANGED", {TEMPERATURE = 99})`