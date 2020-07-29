## PANEL PARTITION STATE

Lets the panel know the state of the given partition.  This is used in the  Properties display in ComposerPro.


| Parameter | Description |
| --- | --- |
| num | PARTITION\_ID: ID of the target partition. |
| str | STATE: A string listing its state. Supported values include: "ARMED" "ALARM" "OFFLINE" "EXIT\_DELAY" "ENTRY\_DELAY" "DISARMED\_READY" "DISARMED\_NOT\_READY" "CONFIRMATION\_REQUIRED" |
| str | TYPE:  Further information on the state. For example, it could be "Stay" for a type of ARMED. It could be "Burglary" for a type of ALARM. Can be "" if not needed. |


### Example

```lua
C4:SendToProxy(5001, "PANEL_PARTITION_STATE", {PARTITION_ID = 2, STATE = "ARMED", TYPE = "Stay"}, "NOTIFY")
```
