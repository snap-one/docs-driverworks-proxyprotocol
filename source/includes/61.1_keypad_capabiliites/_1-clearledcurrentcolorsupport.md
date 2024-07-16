## clear\_led\_current\_color\_support

Enabling this capability allows the Keypad Proxy to clear keypad button(s) color. Previously, this had to be done at the protocol level. Specifically, this is applicable to button colors that have been set programmatically in Composer Pro. Enabling this capability in your driver will expose two new Keypad Proxy Programming Action in Composer Pro: Clear LED Current and Clear All LED Current.

###### Available from 3.4.2.

### Signature

`<clear_led_current_color_support></clear_led_current_color_support>`


### Type

Boolean. Defaults to false


### Dynamic Capability

No

### Usage Note

In conjunction with this capabilities’ use, Drivers need to implement the following Proxy Commands:

[KEYPAD\_BUTTON\_COLOR\_CLEAR][1] - A Notify must be sent when this command is received containing the new button color for the indicated button using the KEYPAD\_BUTTON\_COLOR notification.

[KEYPAD\_ALL\_BUTTON\_COLOR\_CLEAR][2] - A Notify must be sent when this command is received containing the new button colors for each button using the KEYPAD\_BUTTON\_COLOR notification.


### Example

```xml
<capabilities>
    <clear_led_current_color_support>true</clear_led_current_color_support>
</capabilities>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#keypad-proxy-commands-keypad_button_color_clear
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#keypad-proxy-commands-keypad_all_button_color_clear