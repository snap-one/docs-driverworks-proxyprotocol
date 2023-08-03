## has\_level

A boolean capability indicating if the blind can support reporting of discrete level values through Notifications.  Default to False in order for older drivers to work.


### Signature

`<has_level></has_level>`


| Parameter | Description |
| --- | --- |
| bool | True/False |


### Usage Note

If stop is not supported 0 is closed and 1 is open. 

If stop is supported 0 is closed and 1 is somewhere in the middle depending when stop is pressed and 2 for open.

If a blind supports closed, 4 distinct middle levels, and open then 0 is closed, 1-4 would be the distinct levels, and 5 would be open.

Reporting discrete values is possible even if accepting discrete commands is not. Presets, timers, or other formulas can be used to report discrete values.


### Example

```xml
<capabilities>
    <has_level>true</has_level>
</capabilities>
```

