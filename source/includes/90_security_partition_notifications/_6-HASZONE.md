## HAS\_ZONE

Tells the proxy that a particular zone is part of this partition.


| Parameter | Description |
| --- | --- |
| num | ZONE\_ID: The zone ID of the zone to be included in this partition's zone list. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "HAS_ZONE", { ZONE_ID = 2 }, "NOTIFY")
```
