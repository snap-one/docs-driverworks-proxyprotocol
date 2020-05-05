## HAS AIR CHANGED

Sent to the proxy to indicate that there is an outdoor air temperature available on this pool controller.  Determines whether the outdoor temperature is shown on the Navigator UI.


### Signature

`C4:HAS_AIR_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `HASAIR` | (“True/False”) |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "HASAIR_CHANGED", {HASAIR = "True"})`
