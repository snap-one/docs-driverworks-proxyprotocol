## brightness\_on\_mode\_previous

Used to enable the Previous On "On Mode" behavior for a light. The 3.3.2 and newer proxies track the last brightness non-zero level reported by a driver before a BRIGHTNESS\_CHANGED notification occurs with a level of 0. When the proxy gets a generic On (aka Dynamic On) then the proxy will send a SET\_BRIGHTNESS\_TARGET command with that last reported non-zero brightness level. The proxy will also update the PREVIOUS brightness preset value with the last non 0 brightness level anytime the proxy gets a BRIGHTNESS\_CHANGED notify of a value of 0.

Additionally if drivers get a command to turn on that did not come from the proxy, the driver can check the brightness PREVIOUS preset value to know what level it should turn on to.


### Signature

`<brightness_on_mode_previous></brightness_on_mode_ previous>`


### Type

Boolean. Defaults to false


### Dynamic Capability

No


### Example

```xml
<capabilities>
    <brightness_on_mode_previous>true</brightness_on_mode_previous>
</capabilities>
```
