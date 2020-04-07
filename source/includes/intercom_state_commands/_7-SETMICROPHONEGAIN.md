## SET MICROPHONE GAIN

This command is issued by a proxy consumer to cause the microphone gain for the indicated intercom device to change.  This command will result in a `MICROPHONE_GAIN_CHANGED` notification to the indicated device. 


### Signature

`C4: SET_MICROPHONE_GAIN ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```
<SET_MICROPHONE_GAIN>
    <microphoneGain>[0]</microphoneGain>
</SET_MICROPHONE_GAIN>
```
