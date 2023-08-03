## level\_unknown

Integer indicating the level value that is to be specified as "unknown blind position".  This is often, but not always, a value outside of the range of valid level values.  This allows a driver that is initializing (not yet communicating with the blind),  lost communication or for any other reason does not know the exact location of the blind to notify Director that the current level is unknown.


### Signature

`<level_unknown></level_unknown>`


### Example


```xml
<capabilities\>
    <level_unknown>11</level_unknown>
</capabilities>
```
