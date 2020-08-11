## EXECUTE_FUNCTION

Command from the UI to the Proxy and then forwarded on to the Protocol. Has no Return values. Request the partition to execute a function event of the type listed in the functions capability. The function parameter would be one of the function strings listed in the `GET_SETUP` xml.


| Parameter | Description |
| --- | --- |
| str | Function. |
| str | InterfaceID:  A unique string to identify which interface is sending this command. |


### Returns

`None`



