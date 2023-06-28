## KEYPAD\_BUTTON\_INFO

Used to change the settings on a particular button.


### Signature

`KEYPAD_BUTTON_INFO ()`


| Parameter | Description |
| --- | --- |
| BUTTON ID | The ID of the button being changed |
| NAME | The name of the button (optional) |
| ON COLOR (string) |  The on/press color for the button (optional) |
| OFF COLOR  (string) |The off/release color for the button (optional) |
| ENGRAVING (string) | The engraved name for the button (optional) |
| BUTTON BEHAVIOR (INT) | The behavior for the button (optional) |
| LED BEHAVIOR (INT) | The LED behavior for the button (optional) |
| STATE (bool) | Used to indicate which color the button should use. A value of true means use the on/push color, a value of false means use the off/release color. |
| MATCH LED STATE | Similar to state, but should only be applied if the LED is tracking a bound device. |



### Returns

`None`
