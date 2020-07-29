## TROUBLE CLEAR

Clear the trouble flag.  


### Signature

`TROUBLE_CLEAR ()`


| Parameter | Description |
| --- | --- |
| num | IDENTIFIER:  Unique number for the trouble instance that has been resolved. | \_ 

### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "TROUBLE_CLEAR", { IDENTIFIER = 10 }, "NOTIFY")
```

