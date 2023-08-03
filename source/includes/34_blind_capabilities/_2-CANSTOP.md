## can\_stop

Capability to stop movement of blinds


### Signature

`<can_stop></can_stop>`


| Parameter | Description |
| --- | --- |
| bool | True/False |


### Usage Note

This capability was delivered pre-2.9.0. It is still supported by the latest version of the proxy for drivers that do not have the `has_level capbility` defined.


### Example

```xml
<capabilities>
   <can_stop>true</can_stop>
</capabilities>
```
