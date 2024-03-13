## POOL\_TEMP\_CHANGED

Sent to the proxy to indicate that the pool temperature has changed.


### Name

`POOL_TEMP_CHANGED ()`


| Parameter     | Type | Description            |
| ------------- | ---- | ---------------------- |
| `TEMPERATURE` | NUM  | New temperature value. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "POOL_TEMP_CHANGED", {TEMPERATURE = 78})`
