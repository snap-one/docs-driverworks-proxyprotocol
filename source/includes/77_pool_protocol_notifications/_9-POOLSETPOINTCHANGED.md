## POOL\_SETPOINT\_CHANGED

Sent to the proxy to indicate that the setpoint on the pool controller has changed.


### Name

`POOL_SETPOINT_CHANGED ()`


| Parameter  | DType | Description   |
| ---------- | ----- | ------------- |
| `SETPOINT` | NUM   | New setpoint. |


### Returns

`None`

### Example

`C4:SendToProxy(5001, "POOL_SETPOINT_CHANGED", {SETPOINT = 23})`