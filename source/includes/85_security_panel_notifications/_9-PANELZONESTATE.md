## PANEL ZONE STATE

Sends the current status of a zone:  open or closed.


| Parameter | Description |
| --- | --- |
| num | ZONE\_ID: ID of the target zone |
| bool | ZONE\_OPEN: "true" if the zone is opened. "false" if it is closed. |
| bool | INITIALIZING: "true" if the zone is initializing. This will prevent programming from firing. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ZONE_STATE", { ZONE_ID = 1, ZONE_OPEN = true, INITIALIZING = false }, "NOTIFY")
```
