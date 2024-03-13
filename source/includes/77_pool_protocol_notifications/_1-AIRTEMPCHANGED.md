## AIR\_TEMP\_CHANGED

Sent to the proxy to indicate that the air temperature has changed


### Name

`AIR_TEMP_CHANGED ()`


| Parameter     | Type | Description        |
| ------------- | ---- | ------------------ |
| `TEMPERATURE` | NUM  | Temperature value. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "AIR_TEMP_CHANGED", {TEMPERATURE = 99})`