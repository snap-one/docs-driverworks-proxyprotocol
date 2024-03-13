## TROUBLE\_CLEAR

Clear the trouble flag.  


| Parameter  | Type | Description                                                    |
| ---------- | ---- | :------------------------------------------------------------- |
| IDENTIFIER | NUM  | Unique number for the trouble instance that has been resolved. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "TROUBLE_CLEAR", { IDENTIFIER = 10 }, "NOTIFY")
```

