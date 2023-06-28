## level\_open

Integer indicating the open level of the control surface.  Defaults to 1 and must be a higher integer than `level_closed`. This capability is only needed if [`has_level`][1] is set and the value is other than 1.  For example, if the blind control supports adjustments every 5%, use 20.)


### Signature

`<level_open></level_open>`


### Example

```xml
<capabilities>
    <level_open>1</level_open>
</capabilities>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#has-level