## PARTITION ENABLED

It's possible to have partitions defined on a panel that aren't enabled. They still must have a proxy defined for them, but it is possible to specify whether they are currently in use or not.


| Parameter | Description |
| --- | --- |
| bool | ENABLED: "true" if this partition is enabled. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PARTITION_ENABLED", { ENABLED = tostring(Enabled) }, "NOTIFY")
```
