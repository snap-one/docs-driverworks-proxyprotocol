## NUM\_AUXS\_CHANGED

Sent to the proxy to indicate the number of Aux Buttons available in ComposerPro, and on Navigator


### Signature

`NUM_AUXS_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `AUXS` | Maximum number of auxiliaries. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "NUM_AUXS", {AUXS = 5}`

