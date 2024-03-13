## PANEL\_PGM\_STATE

Current status of a PGM (relay): open or closed


| Parameter    | Type | Description                                                                   |
| ------------ | ---- | ----------------------------------------------------------------------------- |
| PGM ID       | NUM  | ID of the target PGM                                                          |
| PGM OPEN     | BOOL | "true" if the PGM is opened. "false" if it is closed.                         |
| INITIALIZING | BOOL | "true" if the PGM is initializing. This will prevent programming from firing. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_PGM_STATE", { PGM_ID = 1, PGM_OPEN = true, INITIALIZING = false }, "NOTIFY")
```
