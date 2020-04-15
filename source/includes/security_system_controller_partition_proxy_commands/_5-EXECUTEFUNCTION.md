## EXECUTE FUNCTION

Command from the UI to the Proxy and then forwarded on to the Protocol. Has no Return values. Request the partition to execute a function event of the type specified by the Function parameter. The function parameter would be one of the function strings listed in the `GET_SETUP` xml.


### Signature

`C4:EXECUTE_FUNCTION ()`


| Parameter | Description |
| --- | --- |
| str | Function. |
| str | Parameters: A space delimited string that contains any parameters that this particular function may require such as a user code. |
| str | InterfaceID:  A unique string to identify which interface is sending this command. |


### Returns

`None`



