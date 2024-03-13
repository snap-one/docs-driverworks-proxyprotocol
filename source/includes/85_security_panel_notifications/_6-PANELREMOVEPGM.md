## PANEL\_REMOVE\_PGM

Remove a PGM (relay) from the panel.


| Parameter | Type | Description                 |
| --------- | ---- | --------------------------- |
| PGM ID    | NUM  | ID of the PGM being removed |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_REMOVE_PGM", { PGM_ID = 1 }, "NOTIFY")
```
