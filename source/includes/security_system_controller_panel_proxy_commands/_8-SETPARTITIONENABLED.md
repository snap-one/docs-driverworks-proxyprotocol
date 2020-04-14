## SET PARTITION ENABLED

This command is received from the UI and then forwarded to the protocol driver to set the enabled flag for an individual partition.


### Signature

`C4:SET_PARTITION_ENABLED ()`


| Parameter | Description |
| --- | --- |
| int | PARTITION ID: 1-n ID of the affected partition. |
| bool | ENABLED: True if this partition is now enabled. |
| str | USERCODE: Optional user code that may be needed to execute this command. |


### Returns

`None
`
