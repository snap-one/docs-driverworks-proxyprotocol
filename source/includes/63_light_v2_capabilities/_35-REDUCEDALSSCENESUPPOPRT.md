## reduced\_als\_support

If the advanced\_scene\_support capability is false, a driver can use this reduced\_als\_support capability for Advanced Lighting Scene support. The device will be allowed into a scene, but the device can't participate in scene ramping and can only have either 0 or 1 elements in a scene. 


### Signature

`<reduced_als_support></reduced_als_support>`


### Type

Boolean: Defaults to false.


### Dynamic Capability

No

### Example

```xml
<capabilities>
  <reduced_als_support>false</reduced_als_support>
</capabilities>
```
