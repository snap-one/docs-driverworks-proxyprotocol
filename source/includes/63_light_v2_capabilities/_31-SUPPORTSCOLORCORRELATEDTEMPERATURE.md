## supports\_color\_correlated\_temperature

Wh Whether the device has native support for color correlated temperature reporting in Kelvin. Set this capability to False if the driver can only do predefined color temperatures. If enabled via dynamic capability, it will be necessary  to Notify the proxy of the current color immediately after the capability is enabled. 


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


### Usage Note

Note: If changing the supports\_color or supports\_color\_correlated\_temperature capabilities via the Dynamic Capabilities Notify, these should both be done in a single notification. If only one is disabled/enabled at a time, device color presets such as the On or Dim colors)may have their color mode changed between Full Color and CCT automatically. 

For example, if the presets mode were Full Color and a driver on director startup dynamically enabled just supports\_color\_correlated\_temperature then the proxy would detect that Full Color is not supported and change any existing presets to color mode CCT.