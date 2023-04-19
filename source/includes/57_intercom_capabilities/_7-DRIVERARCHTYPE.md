## driver arch type
This is a legacy capability that was needed for older Control4 devices that used echo cancellation. Its use is not applicable to external, third party driver development efforts.


### Signature

`<driver_arch_type></driver_arch_type>`


| Parameter | Description |
| --- | --- |
| num | 0-5. Device Type Number |


### Example

```xml
<capabilities>
   <driver_arch_type>3</driver_arch_type>
</capabilities>
```
