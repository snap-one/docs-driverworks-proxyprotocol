## driver\_handles\_toggle

Capability to stop movement of blinds


### Signature

`<driver_handles_toggle></driver_handles_toggle>`


| Parameter | Description |
| --- | --- |
| bool | True/False |


### Usage Note

This capability defaults to false. If false, the proxy will handle the toggle commands (which sends `SET_LEVEL_TARGET` commands to the driver) or if true will send a `LEVEL_TOGGLE` command to the driver so the driver can handle toggle as it desires.

We strongly recommend driver developers do not set this to true unless they absolutely must. Inconsistencies will occur if there are a mix of different driver types in a blind group. This will cause blinds to move differently when that group is commanded to toggle.  

The blind proxy has logic that treats toggle the same as lights in Control4.  If a blind is not moving but open any amount and someone presses toggle, the proxy will always send a [`SET_LEVEL_TARGET`][1] of the closed value.  This is due to the high possibility of someone entering a room and not knowing what direction the blind previously moved. However, if a blind is currently in motion and someone presses toggle, the proxy will send [`SET_LEVEL_TARGET`][2] of the opposite direction that the blind is moving. This has the most natural use of toggle for real-world scenarios.

### Example

```xml
<capabilities>
   <driver_handles_toggle>true</driver_handles_toggle>
</capabilities>
```


[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#blind-proxy-commands-set_level_target
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#blind-proxy-commands-set_level_target