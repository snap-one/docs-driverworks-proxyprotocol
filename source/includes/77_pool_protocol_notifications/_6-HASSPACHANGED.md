## HAS\_SPA\_CHANGED

Sent to the proxy to indicate that there is a Spa available on this controller. If ‘False’, Spa Setpoint is unavailable to set.


### Name

`HAS_SPA_CHANGED ()`


| Parameter | Type | Description                                           |
| --------- | ---- | ----------------------------------------------------- |
| `HASSPA`  | BOOL | (“True/False”) Is a Spa available on this controller. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "HASSPA_CHANGED", {HASSPA = "True"})`
