## EMERGENCY\_TRIGGERED

An emergency was triggered, either from a sensor or by the user hitting one of the emergency buttons.


| Parameter | Description |
| --- | --- |
| str | TYPE: Specifies the type of emergency just triggered.  It can be anything, but standard types that Navigator has icons for are: Fire, Medical, Police, and Panic. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "EMERRGENCY_TRIGGERED", { TYPE = "Fire" }, "NOTIFY")
```
