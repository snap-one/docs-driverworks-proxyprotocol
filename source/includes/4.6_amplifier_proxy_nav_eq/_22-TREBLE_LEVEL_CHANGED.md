## TREBLE\_LEVEL\_CHANGED

Navigator EQ notification that the treble level has changed.


### Signature

`TREBLE_LEVEL_CHANGED`


| Parameter | Type | Description                           |
| --------- | ---- | ------------------------------------- |
| OUTPUT    | int  | Output Binding ID                     |
| LEVEL     | int  | New treble level. Range is -12 to 12. |


### Returns

`None`


### Example

```lua
-- Notify Treble Level is at -6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "TREBLE_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = -6 }, "NOTIFY")


-- Notify Treble Level is at +6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "TREBLE_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = 6 }, "NOTIFY")
```
