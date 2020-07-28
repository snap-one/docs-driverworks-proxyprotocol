## DISARM FAILED

An attempt to disarm the panel failed typically due to  an invalid user code.


### Signature

`DISARM_FAILED ()`


| Parameter | Description |
| --- | --- |
| str | NTERFACE_ID: Commands receiveD from Director will have an interface_id string sent as one of the parameters.  This is a unique string that identifies where the command originated. When a response such as a failure is sent, it should only display on the UI that originated the command.  To support this, the INTERFACE_ID string is sent back with the notification. Only the original UI will show the results of this notification. |


### Returns

`None`


### Example