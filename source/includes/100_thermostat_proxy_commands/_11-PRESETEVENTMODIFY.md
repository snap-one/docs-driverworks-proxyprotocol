## PRESET\_EVENT\_MODIFY

Modifies an existing Preset Schedule Event (If protocol driver has the `can_preset_schedule` capability)


### Name

`PRESET_EVENT_MODIFY ()`


| Parameter   | Type | Description              |
| ----------- | ---- | ------------------------ |
| NAME        | STR  | Event Name               |
| WEEKDAY:    | INT  | 0-6 with Sunday being 0. |
| HOUR        | INT  | 0-23                     |
| MINUTE      | INT  | 0-60                     |
| NEW WEEKDAY | INT  | 0-6 with Sunday being 0  |
| NEW HOUR    | INT  | 0-23                     |
| NEW MINUTE  | INT  | 0-60                     |


### Returns

`None`


### Usage Note

Modifying an event to the same time as a different preset event will result in the different preset event being deleted and the new one being put in at that time.


