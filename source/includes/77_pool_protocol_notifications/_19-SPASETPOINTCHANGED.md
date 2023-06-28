## SPA\_SETPOINT\_CHANGED

Sent to the proxy to indicate that the temperature setpoint on the spa controller has changed.


### Signature

`SPA_SETPOINT_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `SETPOINT` | New setpoint value. |


### Returns

`None`

### Example

`C4:SendToProxy(5001, "SPA_SETPOINT_CHANGED", {SETPOINT = 103}) `