## driver\_arch\_type

This capability is included in the SDK for Control4 internal use. It is used to determine if the driver file is a Control4 driver or a third party driver. **Third party driver developers must pass a value of 5 in this capability.**


### Signature

`<driver_arch_type></driver_arch_type>`


| Parameter | Description             |
| --------- | ----------------------- |
| num       | 0-5. Device Type Number |


### Example

```xml
<capabilities>
   <driver_arch_type>5</driver_arch_type>
</capabilities>
```
