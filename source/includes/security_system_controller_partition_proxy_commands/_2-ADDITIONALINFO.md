## ADDITIONAL INFO

Command from the UI to the Proxy and then forwarded on to the Protocol. Has no Return values. This command will only be sent after having received a `REQUEST_ADDITIONAL_INFO` notification from the protocol driver.  The protocol driver will send the notification to the proxy driver, which will send a `request_additional_info` DataToUI command to the UIs.  The UIs will then prompt the user for additional info. After the information is entered, the UI will generate this command to send back to the protocol driver. See the `REQUEST_ADDITIONAL_INFO` notification.


### Signature

`C4:ADDITIONAL_INFO ()`


| Parameter | Description |
| --- | --- |
| str | Info: A copy of the `info_string` parameter that was passed with the `request_additional_info` request. The protocol driver will need this to know what actions to return to when it gets the new info. |
| str | FunctionName:  A copy of the `function_name` parameter that was passed with the `request_additional_info` request. The protocol driver may need this to know what actions to return to when it gets the new info. |
| str | NewInfo: The new info provided by the UI in response to the `equest_additional_info` request. |
| str | InterfaceID: A unique (str) to identify which interface is sending this command. |


### Returns

`None`


