## LIGHT LEVEL

Used to inform the proxy that the light level has changed.  This notify should not be used with the new supports_brightness_target API that supports LIGHT_BRIGHTNESS_CHANGING and LIGHT_BRIGHTNESS_CHANGED notifies for better ramp tracking.

### Signature

`C4:LIGHT_LEVEL ()`



| Parameter | Description |
| --- | --- |
| int | LEVEL: Percent from 0-100 of the current light level. |


### Returns

`None`