## NUM\_AUXS\_CHANGED

Sent to the proxy to indicate the number of Aux Buttons available in ComposerPro, and on Navigator


### Name

`NUM_AUXS_CHANGED ()`


| Parameter | Type | Description                    |
| --------- | ---- | ------------------------------ |
| `AUXS`    | NUM  | Maximum number of auxiliaries. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "NUM_AUXS", {AUXS = 5}`

