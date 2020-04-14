## HAS SPA CHANGED

Sent to the proxy to indicate that there is a Spa available on this controller. If ‘False’, Spa Setpoint is unavailable to set.


### Signature

`C4:HAS_SPA_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `HASSPA` | (“True/False”) |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "HASSPA_CHANGED", {HASSPA = "True"})`
 `
`
