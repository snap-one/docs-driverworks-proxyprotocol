## PANEL REMOVE PGM

Remove a PGM (relay) from the panel.


### Signature

`PANEL_ADD_PGM ()`


| Parameter | Description |
| --- | --- |
| num | PGM\_ID: ID of the PGM being removed |


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_REMOVE_PGM", { PGM_ID = 1 } "NOTIFY")
```
