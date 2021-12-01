## C4.sendCommand

Sends a command to either the protocol or driver. All responses are sent back via the Javascript callback: `onDataToUi(response: string)`. Driver writers will need to implement this callback in their web page. Errors are sent back via:  `onSendCommandError(message: string)`


### Signature

`C4.sendCommand(commandName: string, params: string, async: boolean, sendToProtocol: boolean = false): void)`


| Parameter | Description |
| --- | --- |
| string | _commandName_ - The name of the command to be executed by the driver or protocol. |
| string | _params_ - A JSON formatted string of parameters. Invalid JSON will trigger an exception. |
| boolean | _async_ -  `true` to send the command asynchronously to ExecuteCommand(). `false` to send the command as a UI Request.  |
| boolean | _sendToProtocol_ - Whether the command should be sent to the protocol or driver. |


| Returns | Description |
| --- | --- |
| _void_ | All responses, even for synchronous commands, will be sent back via the Javascript callback: `onDataToUi(response: string)` |


| Callbacks | Description |
| --- | --- |
| `onDataToUi(response: string)` | Callback to receive DATA\_TO\_UIs when subscribed. |
| `onSubscribeToDataToUiError(message: string)` | Callback to receive error messages when attempting to subscribe to DATA\_TO\_UIs. |


### Example

`C4.sendCommand("SetState", "{'state':'" + color + "'}", false, true);`