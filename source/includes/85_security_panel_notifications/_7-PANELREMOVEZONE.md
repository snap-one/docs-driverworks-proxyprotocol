## PANEL\_REMOVE\_ ZONE

Remove a zone from the panel.  


| Parameter | Description |
| --- | --- |
| num | ID: ID of the target zone. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_REMOVE_ZONE", { ID = 2}, "NOTIFY")
```
