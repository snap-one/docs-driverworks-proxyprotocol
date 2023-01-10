## brightness rate max

Minimum color rate, in milliseconds, supported for transitioning from one brightness to another.  Should always be set for any color light driver, even if the transition rate is unchangeable. Allows dealers to configure the maximum rate that can be configured by dealers. The brightness\_rate value is used by voice control, navigators, customer created advanced lighting scenes, and various other areas of the system that previously didn't allow customization of the transition rate.

Dealers can set the values for this in ComposerPro Properties.


### Signature

`<brightness_rate_max></brightness_rate_max>`


### Type

Integer. Defaults to UNIT16\_MAX. Valid values fall between 0 and 4294967295.


### Dynamic Capability

Yes


### Example

```xml
<capabilities>
    <brightness_rate_max>4294967295</brightness_rate_max>
</capabilities>
```
