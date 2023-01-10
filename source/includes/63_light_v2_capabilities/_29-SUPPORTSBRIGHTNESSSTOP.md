## supports\_brightness\_stop

Used to indicate if a light brightness transition can be stopped during a ramp. Drivers that support Daylight Agent benefit from implementing this as the Daylight scenario can be stopped without having to force a light to go to a different brightness or color to end tracking. Reduced ALS support drivers should implement this capability so that ramping scenes works correctly.

\*Note, a bug in 3.3.2 prevents keypad buttons bound to the proxies BUTTON\_LINK for Brightness Stop from working. This will be resolved in 3.3.3.

### Signature

`<supports_brightness_stop></supports _brightness_stop>`


### Type

Boolean: Defaults to false.


### Dynamic Capability

Yes


### Example

```xml
<capabilities>
    <supports_color>false</supports_color>
</capabilities>
```


### Usage Note

If changing the supports\_color or supports\_color\_correlated\_temperature capabilities via the Dynamic Capabilities Notify, these should both be done in a single notification. If only one is disabled/enabled at a time, device color presets such as the On or Dim colors may have their color mode changed between Full Color and CCT automatically.

For example,  if the presets mode were CCT and a driver on director startup dynamically enabled just supports\_color the proxy would detect that CCT is not supported and change any existing presets to color mode Full Color.