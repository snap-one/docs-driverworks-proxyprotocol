## SYNC PANEL INFO 

This is a request to the proxy driver to re-send all of the information it has about the panel to ensure synchronization.


### Signature

`SYNC_PANEL_INFO ()`


### Parameters

`None`


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "SYNC_PANEL_INFO", {}, "NOTIFY")
```

