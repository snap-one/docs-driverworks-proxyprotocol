## SET\_SEND\_VIDEO

This command is issued by a proxy consumer to cause the state of the send video setting to change.  This command will result in a [`SEND_VIDEO_CHANGED`][1]


### Signature

`SET_SEND_VIDEO ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<SET_SEND_VIDEO>
   <sendVideo>[1]</sendVideo>
</SET_SEND_VIDEO>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#send-video-changed