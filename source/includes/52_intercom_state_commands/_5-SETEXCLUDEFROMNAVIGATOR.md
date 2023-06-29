## SET\_EXCLUDE\_FROM\_NAVIGATOR

This command is issued to toggle the visibility of the intercom endpoint in a proxy user interface. This command will result in an [`EXCLUDE_FROM_NAVIGATOR_CHANGED`][1] notification to the proxy.


### Signature

`SET_EXCLUDE_FROM_NAVIGATOR ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<SET_EXCLUDE_FROM_NAV>
   <excludeFromNav>[1]</excludeFromNav>
</SET_EXCLUDE_FROM_NAV>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-state-notifications-exclude_from_navigator_changed