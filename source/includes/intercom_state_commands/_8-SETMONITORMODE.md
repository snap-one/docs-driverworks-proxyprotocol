## SET MONITOR MODE

This command will result in a `MONITOR_MODE_CHANGED` notification to the proxy consumer for the indicated intercom device.


### Signature

`C4: SET_ MONITOR_MODE ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```
<SET_MONITOR_MODE>
    <monitorMode>[0]</monitorMode>
</SET_MONITOR_MODE>
```
