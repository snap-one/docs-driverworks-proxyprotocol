## level\_discrete\_control

Boolean indicating if a control surface can be set by a COMMAND to something other than the level for closed and the level for open.

If false, a UI will only send [level\_closed][1] and [level\_open][2] integer values to the proxy/driver. However, a driver could still notify various levels interpolated based on movement and or duration/time in each direction or using another formula.

If true, the driver should support all level values in the level range. This could be discrete percentages or even include using level values of 1,2,3,... to execute presets.  However, the min (0) and max (X) should always be programmed for close and open levels respectively.


### Signature

`<level_discrete_control</level_discrete_control>`


### Example

```xml
<capabilities>
    <level_discrete_control>true</level_discrete_control>
</capabilities>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#blind-capabilities-level_closed
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#blind-capabilities-level_open