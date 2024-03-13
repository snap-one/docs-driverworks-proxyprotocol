## KEYPAD\_BUTTON\_INFO

Used to change the settings on a particular button.


### Name

`KEYPAD_BUTTON_INFO ()`


| Parameter       | Type | Description                                                                                                                                        |
| --------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| BUTTON ID       | INT  | The ID of the button being changed                                                                                                                 |
| NAME            | STR  | The name of the button (optional)                                                                                                                  |
| ON COLOR        | STR  | The on/press color for the button (optional)                                                                                                       |
| OFF COLOR       | STR  | The off/release color for the button (optional)                                                                                                    |
| ENGRAVING       | STR  | The engraved name for the button (optional)                                                                                                        |
| BUTTON BEHAVIOR | INT  | The behavior for the button (optional)                                                                                                             |
| LED BEHAVIOR    | INT  | The LED behavior for the button (optional)                                                                                                         |
| STATE           | BOOL | Used to indicate which color the button should use. A value of true means use the on/push color, a value of false means use the off/release color. |
| MATCH LED STATE | BOOL | Similar to state, but should only be applied if the LED is tracking a bound device.                                                                |



### Returns

`None`
