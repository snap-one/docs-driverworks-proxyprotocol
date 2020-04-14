## SPA MODE CHANGED

Sent to the proxy to indicate whether the ‘Spa’ Aux button on the right side of the UI is On or Off.


### Signature

`C4:SPA_MODE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `SPAMODE` | From `<spa_pumpmodes>`True/False |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "SPA_MODE_CHANGED", {SPAMODE = "True"}) `

