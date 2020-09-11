## BUTTON INFO

Used to inform the proxy that a status of a button LED has changed.  Color strings are in the format of 6 hex characters such as 000000, FFFFFF or 0000FF.

### Signature

`C4:BUTTON_INFO ()`


| Parameter | Description |
| --- | --- |
| int | BUTTON_ID: Index of the button being controlled. |
| str | NAME: Optional. Update the name of the button. |
| str | ON_COLOR: Optional. Hex string for the On color. |
| str | OFF_COLOR: Optional. Hex string for the Off color. |
| str | CURRENT_COLOR: Optional. Hex string for the Current color. |



### Returns

`None`