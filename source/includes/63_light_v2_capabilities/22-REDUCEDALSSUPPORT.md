## \_22-REDUCEDALSSUPPORT
## reduced\_als\_support

Whether the device supports the Advanced Lighting Scenes agent, excluding multi-action scene elements.

This capability has been greatly improved for 3.3.2. Most drivers should use this reduced\_als\_support capability as it provides 99% of all lighting scene functionality and doesn't require the driver to implement any ALS API's.

The primary downside of reduced ALS support is the lack of multi-action scene elements.

Drivers using this capability will receive SET\_BRIGHTNESS\_TARGET and SET\_COLOR\_TARGET, SET\_BRIGHTNESS\_STOP, and SET\_COLOR\_STOP commands when a scene is activated rather than ALS API commands.

Drivers should verify that scene ramping via a held scene ramp up/down button works with their drivers via the supports\_target capability and properly handle SET\_COLOR\_STOP and SET\_BRIGHTNESS\_STOP commands.

Note: This cannot be enabled if advanced_scene_support is enabled.


### Signature

`<reduced_als_support></reduced_als_support>`


### Type

Boolean


### Dynamic Capability

No


### Example

```xml
<capabilities>
    <reduced_als_support>false</reduced_als_support>
</capabilities>
```
