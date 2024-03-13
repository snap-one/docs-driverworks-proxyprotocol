## HAS\_POOL\_CHANGED

Sent to the proxy to indicate that there is a Pool available on this controller. If ‘False’, Pool Setpoint is unavailable to set.


### Name

`HAS_POOL_CHANGED ()`


| Parameter | Description | Description                                           |
| --------- | ----------- | ----------------------------------------------------- |
| `HASPOOL` | BOOL        | (“True/False”) Is a Pool available on this controller |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "HASPOOL_CHANGED", {HASPOOL = "True"}) `
