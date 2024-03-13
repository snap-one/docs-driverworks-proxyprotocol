## SPA\_MODE\_CHANGED

Sent to the proxy to indicate whether the ‘Spa’ Aux button on the right side of the UI is On or Off.


### Name

`SPA_MODE_CHANGED ()`


| Parameter | Type | Description                      |
| --------- | ---- | -------------------------------- |
| `SPAMODE` | BOOL | From `<spa_pumpmodes>`True/False |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "SPA_MODE_CHANGED", {SPAMODE = "True"}) `

