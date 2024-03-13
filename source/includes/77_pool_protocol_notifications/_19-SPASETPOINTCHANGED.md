## SPA\_SETPOINT\_CHANGED

Sent to the proxy to indicate that the temperature setpoint on the spa controller has changed.


### Name

`SPA_SETPOINT_CHANGED ()`


| Parameter  | Type | Description         |
| ---------- | ---- | ------------------- |
| `SETPOINT` | NUM  | New setpoint value. |


### Returns

`None`

### Example

`C4:SendToProxy(5001, "SPA_SETPOINT_CHANGED", {SETPOINT = 103}) `