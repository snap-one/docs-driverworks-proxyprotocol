## SET BRIGHTNESS TARGET

Used to set the target brightness of where the light is being requested to go.


### Signature

`SET_BRIGHTNESS_TARGET ()`


| Parameter | Description |
| --- | --- |
| ARG | Target Parameter. One of the following: |
| | Float: LEVEL. Number between min and max as reported by the device | 
| | String: PRESET: Preset Name. |
| | Integer: PERCENT: Percent from 0 to 100 |
| | Integer | RATE: Milliseconds for the transition. Optional. Will use driver default if parameter is not specified. |


### Returns

`None`


