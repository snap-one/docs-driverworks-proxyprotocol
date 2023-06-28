## PRESET\_EVENT\_ADD

Adds a Preset Schedule Preset Event to be run at the specified day/time (If protocol driver has the `can_preset_schedule` capability.


### Signature

`PRESET_EVENT_ADD ()`


| Parameter | Description |
| --- | --- |
| str | NAME |
| int  | WEEKDAY: 0-6 with Sunday being 0 |
| int | HOUR:  0-23 |
| int | MINUTE: 0-60 |


### Returns

`None`


### Usage Note

Adding an event at the same time as a different preset event will result in the different preset event being deleted and the new one being put in at that time.
