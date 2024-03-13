## KEYPAD\_BUTTON\_COLOR

This is used by the protocol to inform the proxy that it has been instructed to change the color of a button.


### Name

`KEYPAD_BUTTON_COLOR ()`


| Parameter     | Type | Description                                                |
| ------------- | ---- | ---------------------------------------------------------- |
| BUTTON ID     | NUM  | The ID of the button whose color is changing.              |
| ON COLOR      | STR  | The new on color for the button in RGB hex string.         |
| OFF COLOR     | STR  | The new off color for the button in RGB hex string.        |
| CURRENT COLOR | STR  | The new current color for the button in RGB hex string.    |
| COLOR         | STR  | The new on and off color for the button in RGB hex string. |


### Returns

`None`
