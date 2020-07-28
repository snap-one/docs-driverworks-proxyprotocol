## REQUEST_ADDITIONAL_INFO

This notification allowS two-way communication with the keypad.  This command will cause Navigator to bring up the keypad screen with the prompt string.  After the user types in something on the keypad, it will be returned to the driver through the ADDITIONAL_INFO command.


### Signature

`REQUEST_ADDITIONAL_INFO ()`


| Parameter | Description |
| --- | --- |
| str | PROMPT: The prompt string that will show up above the keypad on the Navigator string. |
| str | INFO_STRING: This is a string that will not be shown to the user, but will be returned with the ADDITIONAL_INFO command.  It provides a way for information to be built up through multiple iterations of calls to REQUEST_ADDITIONAL_INFO |
| str | FUNCTION_NAME: This will not be shown to the user but will also be returned with the ADDITIONAL_INFO command. It is the function name of the handler in the driver code that should be called when the new information arrives. |
| bool | MASK_DATA: “true" if the information being entered on the screen (such as a user code) should not be readable. If the flag is true, then each character will show up on the Navigator screen as a dot. |
| str | | NTERFACE_ID: Commands receiveD from Director will have an interface_id string sent as one of the parameters.  This is a unique string that identifies where the command originated. When a response such as a failure is sent, it should only display on the UI that originated the command.  To support this, the INTERFACE_ID string is sent back with the notification. Only the original UI will show the results of this notification. | 


### Returns

`None`


### Example