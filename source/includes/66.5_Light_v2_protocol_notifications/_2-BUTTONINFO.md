## BUTTON\_INFO

Used to inform the proxy that a status of a button LED has changed.  Color strings are in the format of 6 hex characters such as 000000, FFFFFF or 0000FF.

### Name

`BUTTON_INFO ()`



| Parameter     | Type | Description                                 |
| ------------- | ---- | ------------------------------------------- |
| BUTTON ID     | INT  | Index of the button being controlled.       |
| NAME          | STR  | Optional. Update the name of the button.    |
| ON COLOR      | STR  | Optional. Hex string for the On color.      |
| OFF COLOR     | STR  | Optional. Hex string for the Off color.     |
| CURRENT COLOR | STR  | Optional. Hex string for the Current color. |



### Returns

`None`