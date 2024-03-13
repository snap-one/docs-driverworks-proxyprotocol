## SPA\_TEMP\_CHANGED

Sent to the proxy to indicate that the spa temperature has changed.


### Name

`SPA_TEMP_CHANGED ()`


| Parameter     | Type | Description            |
| ------------- | ---- | ---------------------- |
| `TEMPERATURE` | NUM  | New temperature value. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "SPA_TEMP_CHANGED", {TEMPERATURE = 105}) `

