## PARTITION STATE INIT

Specifies which state the partition is currently in but will not cause any of the programming to be fired.  


### Signature

`PARTITION_STATE_INIT ()`


| Parameter | Description |
| --- | --- |
| str | STATE: Supported values include: "ARMED" "ALARM" "OFFLINE" "EXIT\_DELAY" "ENTRY\_DELAY" "DISARMED\_READY"
"DISARMED\_NOT\_READY" "CONFIRMATION\_REQUIRED" |
| str | TYPE: Further information on the state. For example, it could be "Stay" for a type of ARMED. It could be "Burglary" for a type of ALARM. Can be "" if not needed. |
| num | DELAY\_TIME\_TOTAL:  For Entry or Exit delays. The total time of the delay. |
| num | DELAY\_TIME\_REMAINING: For Entry or Exit delays, the time remaining in the delay. |
| bool | CODE\_REQUIRED\_TO\_CLEAR: "true" if a user code is now required from Navigator to change from the current state. |


### Returns

`None`


### Example