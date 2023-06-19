## BASS\_LEVEL\_CHANGED

Navigator EQ notification that the bass has changed.


### Signature

`BASS_LEVEL_CHANGED`


| Parameter | Description |
| --- | --- |
| int | OUTPUT: OutputBindingID |
| int | LEVEL: New bass level. Range is -12 to 12. |


### Returns

`None`


### Example

```lua
-- Notify Bass Level is at -6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "BASS_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = -6 }, "NOTIFY") 

-- Notify Bass Level is at +6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "BASS_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = 6 }, "NOTIFY")
```
