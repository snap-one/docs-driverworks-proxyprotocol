## REMOVE\_ZONE

Tells the proxy that a particular zone is no longer a part of this partition.


| Parameter | Type | Description                                                           |
| --------- | ---- | --------------------------------------------------------------------- |
| ZONE ID   | NUM  | The zone ID of the zone to be removed from the partition's zone list. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "REMOVE_ZONE", { ZONE_ID = 1 }, "NOTIFY")
```
