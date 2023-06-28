## NEW\_KEYPAD\_BUTTON

Used to inform the proxy about the existence of a new button on the keypad. If the specified button already exists, this notification will do nothing.


### Signature

`NEW_KEYPAD_BUTTON ()`


| Parameter | Description |
| --- | --- |
| num | BUTTON ID: The ID of the button whose color is changing. |
| str | NAME: The name of the button This will cause binding names to be updated. |
| str | ON COLOR: The new on color for the button in RGB hex string. |
| str | OFF COLOR: The new off color for the button in RGB hex string. |
| str | ENGRAVING: The engraving for the button. |
| num | SLOTS: The size of the button. |
| BUTTON BEHAVIOR | The assigned behavior for this button. |
| LED BEHAVIOR | The assigned behavior of the LED associated with this button. |
| bool | LOCK COLORS:  - Whether the colors for this button should be locked in Composer Pro. TRUE/FALSE Note - The user will not be allowed to change them if True. |


### Returns

`None`
