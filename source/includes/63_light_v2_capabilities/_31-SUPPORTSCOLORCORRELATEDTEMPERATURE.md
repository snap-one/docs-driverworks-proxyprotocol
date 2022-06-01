## supports\_color\_correlated\_temperature

Whether the device has native support for color correlated temperature reporting in Kelvin. Set this capability to False if the driver can only do predefined color temperatures. If enabled via dynamic capability, it will be necessary  to Notify the proxy of the current color immediately after the capability is enabled. 


### Signature

`<supports_color_correlated_temperature></supports_color_correlated_temperature>`


### Type

Boolean: Defaults to false.

### Dynamic Capability

Yes

### Example

```xml
<capabilities>
  <supports_color_correlated_temperature>false<supports_color_correlated_temperature>
</capabilities>
```
