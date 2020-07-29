## REQUEST\_ADDITIONAL\_PANEL\_INFO

This is a notification that can allow two-way communication with the keypad.  This command will cause Navigator to bring up the keypad screen with the prompt string.  After the user types in something on the keypad, it will be returned to our driver through the ADDITIONAL\_PANEL\_INFO command..


### Signature

`REQUEST_ADDITIONAL_PANEL_INFO ()`


| Parameter | Description |
| --- | --- |
| str | PROMPT: The prompt string that will show up above the keypad on the Navigator string. |
| str | INFO\_STRING: This is a string that will not be shown to the user, but will be returned with the [ADDITIONAL\_INFO][1] command.  It is a way that information can be built up through multiple iterations of calls to REQUEST\_ADDITIONAL\_PANEL\_INFO 
|
| str | FUNCTION\_NAME: This will not be shown to the user but will also be returned with the ADDITIONAL\_INFO command. It is the function name of the handler in the driver code that should be called when the new information arrives. |
| bool | MASK\_DATA: “true" if the information being entered on the screen (such as a user code) should not be readable. If the flag is true, then each character will show up on the Navigator screen as a dot. |
| str | INTERFACE\_ID: Unique identification string for one of the UIs that the prompt will appear on. | 


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "REQUEST_ADDITIONAL_PANEL_INFO", { PROMPT = 
promptstring, INFO_STRING = infostring, FUNCTION_NAME = functionstring, MASK_DATA = true, INTERFACE_ID = "interfaceid" } "NOTIFY")
```


[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#additional-info