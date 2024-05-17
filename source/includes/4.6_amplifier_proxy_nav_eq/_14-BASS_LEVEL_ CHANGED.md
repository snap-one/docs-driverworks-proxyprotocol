## BASS\_LEVEL\_CHANGED

Navigator EQ notification that the bass has changed.


### Signature

`BASS_LEVEL_CHANGED`


| Parameter | Type | Description       |
| --------- | ---- | ----------------- |
| LEVEL     | int  | Level             |
| OUTPUT    | int  | Output Binding ID |


### Returns

`None`


### Example

```lua
-- Notify Bass Level is at -6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "BASS_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = -6 }, "NOTIFY") 

-- Notify Bass Level is at +6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "BASS_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = 6 }, "NOTIFY")
```
