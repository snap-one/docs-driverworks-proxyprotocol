## SCALE\_CHANGED

Sent to the proxy to indicate that the Temperature scale has changed.


### Signature

`SCALE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `SCALE` | “C” or “F” |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "SCALE_CHANGED", {SCALE = "C"})`

