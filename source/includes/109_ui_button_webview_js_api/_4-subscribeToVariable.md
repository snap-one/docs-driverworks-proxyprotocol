## C4.subscribeToVariable

Subscribes to the specified variable for either the protocol or proxy. All responses are sent back via the Javascript callback: `onVariable(response: string)`. Driver writers will need to implement this callback in their web page to receive variable change events. Errors are sent back via: `onSubscribeToVariableError(message: string)`



### Signature

`C4.subscribeToVariable("LAST_MENU_SELECTED", false);`


| Parameter | Description |
| --- | --- |
| string | _variableName_ - The name of the variable to subscribe to for either the driver or protocol. |
| boolean | _protocol_ - Whether the variable is part of the protocol (`true`) or proxy (`false`). |


| Returns | Description |
| --- | --- |
| _void_ | All responses will be sent back via the Javascript callback: `onDataToUi(response: string)` |


| Callbacks | Description |
| --- | --- |
| `onVariable(response: string)` | Receives DATA\_TO\_UIs when subscribed. |
| `onSubscribeToVariableError(variableName: string, message: string)` | Receives error messages when attempting to subscribe to a variable. |


### Example

Subscribes to the proxy's "LAST\_MENU\_SELECTED" variable.

`C4.subscribeToVariable("LAST_MENU_SELECTED", false);`