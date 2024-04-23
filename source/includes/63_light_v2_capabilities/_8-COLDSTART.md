## cold\_start

Ramping API indicating if the lighting hardware supports cold start. Defaults to false. In conjunction with O.S. release 3.4.2, this capability was modified to be a Dynamic Capability. This change has no impact on existing drivers using the cold\_start capability. Going forward a driver can now change this capability if needed.

###### Available from 3.4.2.

### Signature

`<cold_start></<cold_start>`


### Type

Boolean


### Dynamic Capability

Yes


### Example

```xml
<capabilities>
    <cold_start>true</cold_start>
</capabilities>
```

```
-- The following command can be sued to dynamically change the cold_start capability: 

C4:SendToProxy(PROXY_ID, 'DYNAMIC_CAPABILITIES_CHANGED', { cold_start = gColdStartEnabled }, "NOTIFY", true)
```
