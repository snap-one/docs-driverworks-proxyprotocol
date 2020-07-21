## ADDITIONAL PANEL INFO

This command is received from the UI and then forwarded to send new information to the requested protocol drive


### Signature

`C4:ADDITIONAL_PANEL_INFO ()`


| Parameter | Description |
| --- | --- |
| str | INFO STRING: The string that was sent along with the request from the protocol driver. |
| str | NEW INFO: The new info that was requested by the protocol driver and was just provided by the UI. |
| str | FUNCTION NAME:  A copy of the `function_name` parameter that was passed with the `request_additional_info` request. The protocol driver may need this to know what actions to return to when it gets the new info. |
| str | INTERFACE ID: Unique string that identifies this instance of the UI. |

### Returns

`None`