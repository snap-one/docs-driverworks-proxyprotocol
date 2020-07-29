## ZONE STATE

Reports if a specific zone is open/closed and bypassed/unbypassed.


| Parameter | Description |
| --- | --- |
| num | ZONE\_ID: Number |
| bool | ZONE\_OPEN: "true" if the zone is opened. "false" if it is closed. |
| bool | ZONE\_BYPASSED: "true" if the zone is bypassed. "false" if it is not bypassed. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "ZONE_STATE", { ZONE_ID = 1, ZONE_OPEN = true, ZONE_BYPASSSED = false }, "NOTIFY")
```
