## ZONE STATE

Reports if a specific zone is open/closed and bypassed/unbypassed.


### Signature

`PARTITION_STATE ()`


| Parameter | Description |
| --- | --- |
| num | ZONE_ID: Number |
| bool | ZONE_OPEN: "true" if the zone is opened. "false" if it is closed. |
| bool | ZONE_BYPASSED: "true" if the zone is bypassed. "false" if it is not bypassed. |


### Returns

`None`


### Example