## PARTITION\_STATE

Specifies which state the partition is currently in.


| Parameter              | Description | Description                                                                                                                                                 |
| ---------------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| STATE                  | STR         | Supported values include: `"ARMED" "ALARM" "OFFLINE" "EXIT_DELAY" "ENTRY_DELAY" "DISARMED_READY" "DISARMED_NOT\\\_READY" "CONFIRMATION_REQUIRED"`           |
| TYPE                   | STR         | Further information on the state. For example, it could be "Stay" for a type of ARMED. It could be "Burglary" for a type of ALARM. Can be "" if not needed. |
| DELAY TIME TOTAL:      | NUM         | For Entry or Exit delays. The total time of the delay.                                                                                                      |
| DELAY TIME REMAINING   | NUM         | For Entry or Exit delays, the time remaining in the delay.                                                                                                  |
| CODE REQUIRED TO CLEAR | BOOL        | "true" if a user code is now required from Navigator to change from the current state.                                                                      |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PARTITION_STATE", { STATE = "ALARM", TYPE = "BURGLARY", DELAY_TIME_TOTAL = 5, DELAY_TIME_REMAINING = 2, CODE_REQUIRED_TO_CLEAR = true }, "NOTIFY")
```
