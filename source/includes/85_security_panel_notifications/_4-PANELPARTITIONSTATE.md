## PANEL\_PARTITION\_STATE

Lets the panel know the state of the given partition.  This is used in the  Properties display in ComposerPro.


| Parameter    | Type | Description                                                                                                                                                                |
| ------------ | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PARTITION ID | NUM  | ID of the target partition.                                                                                                                                                |
| STATE        | STR  | A string listing its state. Supported values include: `"ARMED" "ALARM" "OFFLINE" "EXIT_DELAY" "ENTRY_DELAY" "DISARMED_READY" "DISARMED_NOT_READY" "CONFIRMATION_REQUIRED"` |
| TYPE         | STR  | Further information on the state. For example, it could be "Stay" for a type of ARMED. It could be "Burglary" for a type of ALARM. Can be "" if not needed.                |


### Example

```lua
C4:SendToProxy(5001, "PANEL_PARTITION_STATE", {PARTITION_ID = 2, STATE = "ARMED", TYPE = "Stay"}, "NOTIFY")
```
