## level\_closed\_secondary

Integer indicating how far past open \`(levelopen) the blind can go to a second closed state.   No default value exists for this capability and drivers should not include level\_closed\_secondary if a secondary closed position does not exist.


An example case is a full range louver with 11 positions (0% to 100% with 10% resolution) that has:


-  `level_closed` of 0
- `level_open` of 5
-  `level_close_secondary` of 5


This gives the full close-open-close range of 0 to 10.  

It should be noted that a generic "Close" UI or Composer Programming commands will send the [`level_closed`][1] value for "Close".  No default value exists for this capability and drivers should not include `level_closed_secondary` if a secondary closed position does not exist.


### Signature

`<level_closed_secondary></level_closed_secondary>`


### Example

```xml
<capabilities>
    <level_closed_secondary>11</level_closed_secondary>
</capabilities>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#blind-capabilities-level_closed