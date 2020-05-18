## MUTE CALL

This command can be issued by either the initiator or receiver; the endpoint of the issuer will be muted or un-muted, depending on the value of the flag


### Signature

`C4:MUTE_CALL ()`


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
