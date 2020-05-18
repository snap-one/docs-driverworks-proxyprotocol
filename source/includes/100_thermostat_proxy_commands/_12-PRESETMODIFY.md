## PRESET MODIFY

Modifies an existing Preset Schedule Event (If protocol driver has the `can_preset_schedule` capability)


### Signature

`C4:PRESET_MODIFY ()`


| Parameter | Description |
| --- | --- |
| str | NAME |
| XML | PRESET FIELDS:  XML DATA. |
| str | NEW NAME |

### Returns

`None`


### Example

```lua
<preset_fields>
  <field id="heat_setpoint_f" value="65">
  <field id="cool_setpoint_f" value="75">
  <field id="humidify_setpoint" value="50">
  <field id="fan_mode" value="On">
</preset_fields>
```




