## PANEL\_ZONE\_STATE

Sends the current status of a zone:  open or closed.


| Parameter    | Type | Description                                                                    |
| ------------ | ---- | ------------------------------------------------------------------------------ |
| ZONE ID      | NUM  | ID of the target zone                                                          |
| ZONE OPEN    | BOOL | "true" if the zone is opened. "false" if it is closed.                         |
| INITIALIZING | BOOL | "true" if the zone is initializing. This will prevent programming from firing. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ZONE_STATE", { ZONE_ID = 1, ZONE_OPEN = true, INITIALIZING = false }, "NOTIFY")
```
