## PANEL ADD PGM 

Add a PGM (relay) to the panel.


### Signature

`PANEL_ADD_PGM ()`


| Parameter | Description |
| --- | --- |
| num | PGM\_ID: ID of the new PGM |


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ADD_PGM", { PGM_ID = 1 }, "NOTIFY")
```
