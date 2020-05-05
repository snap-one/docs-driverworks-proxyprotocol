## SPEAKER VOLUME CHANGED

This notification is issued by the proxy when the endpoint’s Speaker Volume setting has changed. 


### Signature

`C4:SPEAKER_VOLUME_CHANGED ()`


| Parameter | Description |
| --- | --- |
| int | The proxy device id of the intercom endpoint whose device state information is being returned |
| num | speakerVol: Numeric indicating the current state for this setting. (0=false, 1=true) |


### Example

```
<device_state proxyid =[10]>
    <speakerVol>[0]</speakerVol>
</device_state>
```

