## PRESET EVENT MODIFY

Modifies an existing Preset Schedule Event (If protocol driver has the `can_preset_schedule` capability)


### Signature

`C4:PRESET_EVENT_MODIFY ()`


| Parameter | Description |
| --- | --- |
| str | NAME |
| int  | WEEKDAY: 0-6 with Sunday being 0. |
| int | HOUR:  0-23 |
| int | MINUTE: 0-60 |
| int | NEW WEEKDAY: 0-6 with Sunday being 0 |
| int | NEW HOUR: 0-23 |
| int | NEW MINUTE: 0-60 |


### Returns

`None`


### Usage Note

Modifying an event to the same time as a different preset event will result in the different preset event being deleted and the new one being put in at that time.


