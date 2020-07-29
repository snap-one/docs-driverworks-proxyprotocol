## PANEL ADD PGM

Add a PGM (relay) to the panel.


| Parameter | Description |
| --- | --- |
| num | PGM\_ID: ID of the new PGM |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ADD_PGM", { PGM_ID = 1 }, "NOTIFY")
```
