## brightness on mode preset

Used to enable generic brightness presets to be used with the "On Mode" behavior.  If a driver supports this capability, it is up to the driver to support additional parameter handling and reporting.

See SET\_BRIGHTNESS\_TARGET, BRIGHTNESS\_CHANGING and BRIGHTNESS\_CHANGED commands and notifies and look for optional parameters such as LIGHT\_BRIGHTNESS\_TARGET\_PRESET\_ID and LIGHT\_COLOR\_CURRENT\_PRESET\_ID.

Additionally, drivers need to implement UPDATE\_BRIGHTNESS\_ON\_MODE and UPDATE\_BRIGHTNESS\_PRESET commands so they can track values for situations where the proxy is not the initiator of light behavior, such as On Mode Fade, scenes, composer programming, etc.


### Signature

`<brightness_on_mode_preset></brightness_on_mode_preset>`


### Type

Boolean. Defaults to false.


### Dynamic Capability

No


### Example

```xml
<capabilities>
    <brightness_on_mode_preset>true</brightness_on_mode_preset>
</capabilities>
```
