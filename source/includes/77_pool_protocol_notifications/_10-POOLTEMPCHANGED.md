## POOL TEMP CHANGED

Sent to the proxy to indicate that the pool temperature has changed.


### Signature

`C4:POOL_TEMP_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `TEMPERATURE` | New temperature value. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "POOL_TEMP_CHANGED", {TEMPERATURE = 78})`
