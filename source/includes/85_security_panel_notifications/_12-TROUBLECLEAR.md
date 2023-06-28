## TROUBLE\_CLEAR

Clear the trouble flag.  


| Parameter | Description |
| --- | --- |
| num | IDENTIFIER:  Unique number for the trouble instance that has been resolved. | \_ 


### Example

```lua
C4:SendToProxy(TargetBindingID, "TROUBLE_CLEAR", { IDENTIFIER = 10 }, "NOTIFY")
```

