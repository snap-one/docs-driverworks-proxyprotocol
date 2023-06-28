## PARTITION\_STATE

Specifies which state the partition is currently in.


| Parameter | Description |
| --- | --- |
| str | STATE: Supported values include: "ARMED" "ALARM" "OFFLINE" "EXIT\_DELAY" "ENTRY\_DELAY" "DISARMED\_READY" "DISARMED\_NOT\_READY" "CONFIRMATION\_REQUIRED"  |
| str | TYPE: Further information on the state. For example, it could be "Stay" for a type of ARMED. It could be "Burglary" for a type of ALARM. Can be "" if not needed. |
| num | DELAY\_TIME\_TOTAL:  For Entry or Exit delays. The total time of the delay. |
| num | DELAY\_TIME\_REMAINING: For Entry or Exit delays, the time remaining in the delay. |
| bool | CODE\_REQUIRED\_TO\_CLEAR: "true" if a user code is now required from Navigator to change from the current state. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PARTITION_STATE", { STATE = "ALARM", TYPE = "BURGLARY", DELAY_TIME_TOTAL = 5, DELAY_TIME_TOTAL = 2, CODE_REQUIRED_TO_CLEAR = true }, "NOTIFY")
```
