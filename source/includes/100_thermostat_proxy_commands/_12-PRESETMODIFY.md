## PRESET\_MODIFY

Modifies an existing Preset Schedule Event (If protocol driver has the `can_preset_schedule` capability)


### Name

`PRESET_MODIFY ()`


| Parameter     | Type | Description     |
| ------------- | ---- | --------------- |
| NAME          | STR  | Preset Name     |
| PRESET FIELDS | XML  | XML DATA        |
| NEW NAME      | STR  | New Preset Name |

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




