## EXECUTE_EMERGENCY

Command from the UI to the Proxy and then forwarded on to the Protocol. Has no Return values. Requests the partition to execute an emergency event of the type specified by the EmergencyType parameter. Valid values are: Fire, Medical, Police, and Panic.


| Parameter | Description |
| --- | --- |
| str |  A unique string to identify which interface is sending this command. |
| str | Interface ID: Unique string ID indicating from where the command originated |



### Returns

`None`



