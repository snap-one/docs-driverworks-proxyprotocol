## dimmer

When set to true the device is a dimmer. If true, the capabilities listed in the Usage Note will be checked.


### Signature

`<dimmer></dimmer>`


### Example

```xml
<capabilities>
   <dimmer>true</dimmer>
</capabilities>
```


### Usage Note

`set_level`  Determines whether commands to directly set the level of the device appear in Composer.

`ramp_level`  Determines whether commands to ramp the device appear in Composer.

`fixed_ramp_rate`  If the device can ramp and isn't user configurable, this is the number of milliseconds it takes to ramp. This is used only by the Advanced Lighting Scenes Agent.

`click_rates`  Determines whether properties appear in Composer allowing the user to set the click rates.

`click_rate_min`  Minimum length of time in milliseconds that can be set for Click Rate. Default 0 milliseconds (2.8+).

`click_rate_max`  Maximum length of time in milliseconds that can be set for Click Rate. Default 1 day of milliseconds (2.8+).

`hold_rates`  Determines whether properties appear in composer allowing the user to set hold rates.

`hold_rate_min`  Minimum length of time in milliseconds that can be set for Hold Rate. Default 1000 milliseconds (2.8+).

`hold_rate_max`  Maximum length of time in milliseconds that can be set for Hold Rate Default 1 day of milliseconds (2.8+).

`cold_start`  Determines whether properties appear in Composer allowing the user to set the cold start time and rate.

`min_max `  Determines whether properties appear in Composer allowing the user to set the min and max on levels for the device.