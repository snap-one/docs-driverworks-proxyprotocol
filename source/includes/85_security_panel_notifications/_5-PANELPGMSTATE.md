## PANEL\_PGM\_STATE

Current status of a PGM (relay): open or closed


| Parameter | Description |
| --- | --- |
| num | PGM\_ID: ID of the target PGM |
| bool | PGM\_OPEN: "true" if the PGM is opened. "false" if it is closed. |
| bool | INITIALIZING: "true" if the PGM is initializing. This will prevent programming from firing. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_PGM_STATE", { PGM_ID = 1, PGM_OPEN = true, INITIALIZING = false }, "NOTIFY")
```
