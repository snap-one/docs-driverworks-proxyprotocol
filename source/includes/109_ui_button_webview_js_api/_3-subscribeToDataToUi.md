## C4.subscribeToDataToUi

Subscribes to the DATA\_TO\_UIs for either the protocol or proxy. All responses are sent back via the Javascript callback: `onDataToUi(response: string)`. Driver writers will need to implement this callback in their web page to receive DATA\_TO\_UIs. Errors are sent back via: `onSubscribeToDataToUiError(message: string)`



### Signature

`C4.subscribeToDataToUi(sendToProtocol: boolean = false):void`

| Parameter | Description |
| --- | --- |
| boolean | _sendToProtocol_ - Whether the command should be sent to the protocol (`true`) or proxy (`false`). |


| Returns | Description |
| --- | --- |
| _void_ | All responses will be sent back via the Javascript callback: `onDataToUi(response: string)` |


| Callbacks | Description |
| --- | --- |
| `onDataToUi(response: string)` | Receives DATA\_TO\_UIs when subscribed. DATA\_TO\_UIs are converted to json by Broker before being sent to the web page. |
| `onSubscribeToDataToUiError(message: string)` | Receives error messages when attempting to subscribe to DATA\_TO\_UIs. |


### Example

Subscribes to the protocol's DataToUI events. Protocol driver's can send DataToUI 
events by calling `C4:SendDataToUI(xml)` or `C4:SendDataToUI (strCommand, tParams)`

`C4.subscribeToDataToUi(true);`