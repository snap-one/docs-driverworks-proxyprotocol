## PANEL REMOVE PGM

Remove a PGM (relay) from the panel.


| Parameter | Description |
| --- | --- |
| num | PGM\_ID: ID of the PGM being removed |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_REMOVE_PGM", { PGM_ID = 1 }, "NOTIFY")
```
