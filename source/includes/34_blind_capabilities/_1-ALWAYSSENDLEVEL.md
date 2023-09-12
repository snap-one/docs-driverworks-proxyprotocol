## always\_send\_level

If value is true, then the SetTargetLevel commands are always sent regardless of current level values. This is useful if the blind device does not support two-way communication and is controlled outside of the Control4 operating system. Setting this capability to True ensures that the SetTargetLevel values are always available so accurate blind performance can occur.


### Signature

`<always_send_level></always_send_level>`


| Parameter | Description                   |
| --------- | ----------------------------- |
| bool      | True/False. Defaults to False |


### Example

```xml
<capabilities>
   <always_send_level>true</always_send_level>
</capabilities>
```
