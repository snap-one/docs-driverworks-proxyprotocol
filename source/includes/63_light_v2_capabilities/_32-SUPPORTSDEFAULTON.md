## supports\_default\_on

This feature is for lights that support a default ON brightness in their firmware. When enabled, the Light Proxy sends a SET\_PRESET\_LEVEL command to drivers when the brightness "On” preset is updated in the proxy through Composer or the PRESET\_LEVEL system variable. This enables light switches that respond to local button presses to go to the same default ON level as what the Control4 system uses when a light is turned on or toggled via Navigators, Composer Programming, and keypad buttons. 


### Signature

`<supports_default_on></supports_default_on>`


### Type

Boolean: Defaults to false.


### Dynamic Capability

No

### Example

```xml
<capabilities>
  <supports_default_on>false<supports_default_on>
</capabilities>
```
