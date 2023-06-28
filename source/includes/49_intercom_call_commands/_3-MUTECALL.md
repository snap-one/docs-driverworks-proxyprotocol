## MUTE\_CALL

Used by Programming or ComposerPro. This command is used to programmatically Mute a device.  TRhe endpoint of the issuer will be muted or un-muted, depending on the value of the flag.


### Signature

`MUTE_CALL ()`


| Parameter | Description |
| --- | --- |
| bool |  muteAudio - A Boolean flag indicating whether to mute or un-mute the indicated session. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<MUTE_CALL>
   <muteAudio>[0]</muteAudio>
</MUTE_CALL>
```
