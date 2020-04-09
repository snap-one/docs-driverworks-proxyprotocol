## KEYPAD BUTTON ACTION

Used by the protocol to inform the proxy that some type of action occurred on a button. The proxy will then update colors, send the proper command to the bound device, etc.


### Signature

`C4:KEYPAD_BUTTON_ACTION ()`


| Parameter | Description |
| --- | --- |
| num | BUTTON ID: The ID of the button to be deleted. |
| NUM |ACTION: The action performed on the keypad: 0 = Release, 1 = Push, 2 = Click, 3 = Double Click, 4 = Triple Click |


### Returns

`None`
