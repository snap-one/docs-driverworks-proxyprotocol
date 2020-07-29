## SYNC PANEL INFO

Tells the Panel proxy that the hardware has been initialized and is ready to function.


### Signature

`PANEL_INITIALIZED ()`


### Parameters

`None`


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_INITIALIZED", {}, "NOTIFY")
```


