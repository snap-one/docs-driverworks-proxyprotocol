## POOL SETPOINT CHANGED

Sent to the proxy to indicate that the setpoint on the pool controller has changed.


### Signature

`POOL_SETPOINT_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `SETPOINT` | New setpoint. |


### Returns

`None`

### Example

`C4:SendToProxy(5001, "POOL_SETPOINT_CHANGED", {SETPOINT = 23})`