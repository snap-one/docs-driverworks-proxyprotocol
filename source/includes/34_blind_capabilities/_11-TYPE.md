## type

Integer representing the enumeration of a type of blind. If set in a driver, the pull-down to select this value will be disabled in the proxy


### Signature

`<type></type>`


| Parameter | Description |
| --- | --- |
| 0 | Shade (Default as all coverings are considered to be Shades in the industry) |
| 1 | Group |
| 2 | Blind (Since a blind has slates/louvers that often move, a blind can be bound to a louver movement for association) |
| 3 | Louvre |
| 4 | Curtain |
| 5 | Shutter |
| 6 | Blackout |
| 7 | Opaque Glass |
| 8 | Awning |
| 9 | Door |
| 10 | Screen |


### Example

```xml
<capabilities>
    <type>6</type>
</capabilities>
```
