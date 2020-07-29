## PANEL_REMOVE_ ZONE

Remove a zone from the panel.  


### Signature

`PANEL_REMOVE_ZONE ()`


| Parameter | Description |
| --- | --- |
| num | ID: ID of the target zone. |


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_REMOVE_ZONE", { ID = 2,}, "NOTIFY")
```
