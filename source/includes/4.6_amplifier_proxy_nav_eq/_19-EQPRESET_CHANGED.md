## EQ\_PRESET\_CHANGED

Navigator EQ notification used when a different preset is selected for an output.  Should be called after SET\_EQPRESET is sent or if the preset is changed from a different event. 



### Signature

`EQPRESET_CHANGED`


| Parameter | Type | Description                                                                                                      |
| --------- | ---- | ---------------------------------------------------------------------------------------------------------------- |
| OUTPUT    | int  | Output Binding ID                                                                                                |
| EQPRESET  | int  | Newly selected equalizer index. Range is 0 to maximum number defined in the  `<eq_preset_nav_count>` capability. |


### Returns

`None`


### Example

```lua
-- Notify change of current EQ Preset for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "EQPRESET_CHANGED", { OUTPUT = "4002", EQPRESET = 2 }, "NOTIFY")
```
