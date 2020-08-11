## SET_PARTITION_ENABLED

Set a flag to designate whether or not the specified partition is currently enabled. This command is only available if the ‘can_activate_partitions’ capability is set to ‘true’.


| Parameter | Description |
| --- | --- |
| str | PARTITION_ID: The id number of the targeted partition. |
| bool | ENABLED: ‘True’ if this partition should now be enabled, False if not. |