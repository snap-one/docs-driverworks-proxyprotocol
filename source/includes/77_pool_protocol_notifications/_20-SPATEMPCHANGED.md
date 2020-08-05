## SPA TEMP CHANGED

Sent to the proxy to indicate that the spa temperature has changed.


### Signature

`SPA_TEMP_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `TEMPERATURE` | New temperature value. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "SPA_TEMP_CHANGED", {TEMPERATURE = 105}) `

