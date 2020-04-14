## HAS POOL CHANGED

Sent to the proxy to indicate that there is a Pool available on this controller. If ‘False’, Pool Setpoint is unavailable to set.


### Signature

`C4:HAS_POOL_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `HASPOOL` | (“True/False”) |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "HASPOOL_CHANGED", {HASPOOL = "True"}) `
