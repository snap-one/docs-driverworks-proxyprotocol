## SET\_MONITOR\_MODE

This command will result in a [`MONITOR_MODE_CHANGED`][1] notification to the proxy consumer for the indicated intercom device.


### Signature

`SET_ MONITOR_MODE ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```lua
<SET_MONITOR_MODE>
    <monitorMode>[0]</monitorMode>
</SET_MONITOR_MODE>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-state-notifications-monitor_mode_changed