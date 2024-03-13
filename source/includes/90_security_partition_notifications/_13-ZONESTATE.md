## ZONE\_STATE

Reports if a specific zone is open/closed and bypassed/un-bypassed.


| Parameter     | Description | Description                                                    |
| ------------- | ----------- | -------------------------------------------------------------- |
| ZONE ID       | NUM         | Number                                                         |
| ZONE OPEN     | BOOL        | "true" if the zone is opened. "false" if it is closed.         |
| ZONE BYPASSED | BOOL        | "true" if the zone is bypassed. "false" if it is not bypassed. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "ZONE_STATE", { ZONE_ID = 1, ZONE_OPEN = true, ZONE_BYPASSSED = false }, "NOTIFY")
```
