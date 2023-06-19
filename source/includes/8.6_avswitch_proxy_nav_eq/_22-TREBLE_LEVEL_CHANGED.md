## TREBLE\_ LEVEL\_ CHANGED

Navigator EQ notification that the treble level has changed.


### Signature

`TREBLE_LEVEL_CHANGED`


| Parameter | Description |
| --- | --- |
| int | OUTPUT: OutputBindingID |
| int | LEVEL: LOUDNESS: New treble level. Range is -12 to 12. |


### Returns

`None`


### Example

```lua
-- Notify Treble Level is at -6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "TREBLE_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = -6 }, "NOTIFY")


-- Notify Treble Level is at +6 for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "TREBLE_LEVEL_CHANGED", { OUTPUT = "4002", LEVEL = 6 }, "NOTIFY")
```
