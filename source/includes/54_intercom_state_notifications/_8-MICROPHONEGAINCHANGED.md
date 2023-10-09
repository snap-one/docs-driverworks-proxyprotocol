## MICROPHONE\_GAIN\_CHANGED

This notification is issued by the protocol  when the endpoint’s Microphone Gain setting has changed.


### Signature

`MICROPHONE_GAIN_CHANGED ()`


| Parameter | Description                                                                                   |
| --------- | --------------------------------------------------------------------------------------------- |
| int       | The proxy device id of the intercom endpoint whose device state information is being returned |
| int       | microphoneGain: Numeric value indicating the current value of this setting. (0 to 100)        |


### Example

```lua
<device_state proxyid =[10]>
    <microphoneGain>[0]</microphoneGain>
</device_state>
```

