## NUM AUXS CHANGED

Sent to the proxy to indicate the number of Aux Buttons available in ComposerPro, and on Navigator


### Signature

`C4:NUM_AUXS_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `AUXS` | Maximum number of auxiliaries. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "NUM_AUXS", {AUXS = 5}`

