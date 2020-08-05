## KEYPAD BUTTON INFO

Used by the protocol to inform the proxy of a changed setting for a particular button. It can have multiple parameters, but the only required one is `BUTTON_ID`.


### Signature

`KEYPAD_BUTTON_INFO ()`


| Parameter | Description |
| --- | --- |
| num | BUTTON ID: The ID of the button whose color is changing. |
| str | NAME: The name of the button This will cause binding names to be updated. |
| str | ENGRAVING: The engraving for the button. |
| str | ON COLOR: The new on color for the button in RGB hex string. |
| str | OFF COLOR: The new off color for the button in RGB hex string. |
| str | CURRENT COLOR:  The new current color for the button in RGB hex string. |
| str | COLOR:  The new on and off color for the button in RGB hex string. |
| STATE | The current state of the button, so the proxy knows what color the button is using (state \> 0 means on-color) |
| LED BEHAVIOR | The assigned behavior of the LED associated with this button. |
| BUTTON BEHAVIOR | The assigned behavior for this button. |



### Returns

`None`

