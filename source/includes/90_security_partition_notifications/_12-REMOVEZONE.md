## REMOVE\_ZONE\_

Tells the proxy that a particular zone is no longer a part of this partition.


### Signature

`REMOVE_ZONE ()`


| Parameter | Description |
| --- | --- |
| num | ZONE\_ID: The zone ID of the zone to be removed from the partition's zone list. |


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "REMOVE_ZONE", { ZONE_ID = 1 }, "NOTIFY")
```
