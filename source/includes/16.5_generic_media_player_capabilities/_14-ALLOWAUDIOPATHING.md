## allow\_audio\_pathing
This capability is applicable in the scenario where the AV Switch proxy is included as a secondary proxy to the Generic Media Player Proxy. This is useful  when modeling streaming media devices that require minidrivers. Prior to O.S. 3.4.0, the Generic Media Proxy could not successfully pass audio paths when bound to the AV Switch Proxy. Setting this capability to True allow for audio pathing through the Generic Media Player to the AV Switch Proxy.

### Signature

`<allow_audio_pathing></allow_audio_pathing>`


| Parameter | Description |
| --------- | ----------- |
| bool      | true/false  |


### Returns

`None`


### Example

```xml
<capabilities>
   <allow_audio_pathing>true</allow_audio_pathing>
</capabilities>
```
