## PANEL\_ADD\_PGM

Add a PGM (relay) to the panel.


| Parameter | Description | Description       |
| --------- | ----------- | ----------------- |
| PGM ID    | NUM         | ID of the new PGM |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ADD_PGM", { PGM_ID = 1 }, "NOTIFY")
```
