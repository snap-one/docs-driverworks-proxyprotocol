## HAS\_AIR\_CHANGED

Sent to the proxy to indicate that there is an outdoor air temperature available on this pool controller.  Determines whether the outdoor temperature is shown on the Navigator UI.


### Name

`HAS_AIR_CHANGED ()`


| Parameter | Description | Description                                             |
| --------- | ----------- | ------------------------------------------------------- |
| `HASAIR`  | BOOL        | (“True/False”) Is an outdoor air temperature available. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "HASAIR_CHANGED", {HASAIR = "True"})`
