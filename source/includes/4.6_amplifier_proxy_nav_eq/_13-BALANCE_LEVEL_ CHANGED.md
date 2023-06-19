## BALANCE \_  LEVEL \_  CHANGED

Navigator EQ notification that the balance has changed.


### Signature

`BALANCE_LEVEL_CHANGED`


| Parameter | Description |
| --- | --- |
| int | OUTPUT: OutputBindingID |
| int | LEVEL: New balance level. Range is 0 to 100. |


### Returns

`None`


### Example

```lua
-- Notify Balance level is set to 'Full Left' for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "BALANCE_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = 0 }, "NOTIFY")

 

-- Notify Balance level is set to 'Center' for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "BALANCE_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = 50 }, "NOTIFY")

 

-- Notify Balance level is set to 'Full Right' for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "BALANCE_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = 100 }, "NOTIFY")
```
