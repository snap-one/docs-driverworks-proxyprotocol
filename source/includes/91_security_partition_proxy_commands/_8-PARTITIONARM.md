## PARTITION ARM

Command from the UI to the Proxy and then forwarded on to the Protocol. Has no Return values. Specifies the user code to use with the arm command (if needed).


| Parameter | Description |
| --- | --- |
| str | ArmType: Request the partition to arm. |
| str | UserCode: Optional. Specifies the user code to use with the arm command (if needed). |
| bool |Bypass: Optional. Specify whether currently open zones should be bypassed. |
| str | InterfaceID: A unique string to identify which interface is sending this command. |


### Returns

`None`


