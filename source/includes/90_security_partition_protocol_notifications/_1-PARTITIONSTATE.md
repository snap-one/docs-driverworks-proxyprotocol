## PARTITION STATE

Specifies which state the partition is currently in.


### Signature

`PARTITION_STATE ()`


| Parameter | Description |
| --- | --- |
| str | STATE: Supported values include: "ARMED" "ALARM" "OFFLINE" "EXIT_DELAY" "ENTRY_DELAY" "DISARMED_READY"
"DISARMED_NOT_READY" "CONFIRMATION_REQUIRED" | |
| str | TYPE: Further information on the state. For example, it could be "Stay" for a type of ARMED. It could be "Burglary" for a type of ALARM. Can be "" if not needed. |
| num | DELAY_TIME_TOTAL:  For Entry or Exit delays. The total time of the delay. |
| num | DELAY_TIME_REMAINING: For Entry or Exit delays, the time remaining in the delay. |
| bool | CODE_REQUIRED_TO_CLEAR: "true" if a user code is now required from Navigator to change from the current state. |

### Returns

`None`


### Example