## KEYPAD\_BUTTON\_ACTION

Used by the protocol to inform the proxy that some type of action occurred on a button. The proxy will then update colors, send the proper command to the bound device, etc.


### Name

`KEYPAD_BUTTON_ACTION ()`


| Parameter | TypeDescription | Description                                                                                              |
| --------- | --------------- | -------------------------------------------------------------------------------------------------------- |
| BUTTON ID | NUM             | The ID of the button to be deleted.                                                                      |
| ACTION    | NUM             | The action performed on the keypad: 0 = Release, 1 = Push, 2 = Click, 3 = Double Click, 4 = Triple Click |


### Returns

`None`
