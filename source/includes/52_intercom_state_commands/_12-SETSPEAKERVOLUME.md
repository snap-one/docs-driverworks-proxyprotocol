## SET SPEAKER VOLUME

This command is issued by a proxy consumer to cause the current speaker volume setting to be changed.  This command will result in a [`SPEAKER_VOLUME_CHANGED`][1] notification to the proxy consumer for the indicated intercom device.


### Signature

`C4: SET_SPEAKER_VOLUME ()`


| Parameter | Description |
| --- | --- |
| num | A numeric value 0-100 that indicates the new speaker volume setting |


### Returns

`None`


### Example

```lua
<SET_SPEAKER_VOLUME>
<speakerVol>[50]</speakerVol>
</SET_SPEAKER_VOLUME>
```

[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#speaker-volume-changed