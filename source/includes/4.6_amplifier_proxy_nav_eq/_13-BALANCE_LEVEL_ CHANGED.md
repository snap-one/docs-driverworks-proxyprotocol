## BALANCE\_LEVEL\_CHANGED

Navigator EQ notification that the balance has changed.


### Signature

`BALANCE_LEVEL_CHANGED`


| Parameter       | Type | Description       |
| --------------- | ---- | ----------------- |
| Level           | INT  | Level value       |
| OutputBindingID | INT  | Output Binding ID |


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
