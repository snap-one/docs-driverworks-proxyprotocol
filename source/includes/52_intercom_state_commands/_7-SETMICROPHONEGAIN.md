## SET\_MICROPHONE\_GAIN

This command is issued by a proxy consumer to cause the microphone gain for the indicated intercom device to change.  This command will result in a [`MICROPHONE_GAIN_CHANGED`][1] notification to the indicated device.


### Signature

`SET_MICROPHONE_GAIN ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<SET_MICROPHONE_GAIN>
    <microphoneGain>[0]</microphoneGain>
</SET_MICROPHONE_GAIN>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#microphone-gain-changed