## PANEL\_ZONE\_INFO

Information about a given zone that Navigator or Composer can display.  


| Parameter | Description                                                                                                                                                                                       |     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-- |
| num       | ID: ID of the target zone.                                                                                                                                                                        |     |
| str       | NAME: The zone's name either read from the panel or assigned by the user. Will default to "Zone NN"                                                                                               |     |
| num       | TYPE ID: The type of zone so that the Control4 system can map its sensor binding to a type of sensor. Current valid types with their ids are:                                                     |     |
|           | UNKNOWN	= 0                                                                                                                                                                                       |     |
|           | CONTACT SENSOR= 1                                                                                                                                                                                 |     |
|           | EXTERIOR DOOR= 2                                                                                                                                                                                  |     |
|           | EXTERIOR WINDOW= 3                                                                                                                                                                                |     |
|           | INTERIOR DOOR	= 4                                                                                                                                                                                 |     |
|           | MOTION SENSOR = 5                                                                                                                                                                                 |     |
|           | FIRE = 6                                                                                                                                                                                          |     |
|           | GAS = 7                                                                                                                                                                                           |     |
|           | CARBON MONOXIDE	= 8                                                                                                                                                                               |     |
|           | HEAT = 9                                                                                                                                                                                          |     |
|           | WATER = 10                                                                                                                                                                                        |     |
|           | SMOKE = 11                                                                                                                                                                                        |     |
|           | PRESSURE = 12                                                                                                                                                                                     |     |
|           | GLASSBREAK= 13                                                                                                                                                                                    |     |
|           | GATE = 14                                                                                                                                                                                         |     |
|           | GARAGE DOOR = 15                                                                                                                                                                                  |     |
| str       | PARTITIONS: Comma-delimited string of numbers indicating which partitions this zone is a  member of.  For example, if this zone is included in both partitions 1 and 3, the string would be "1,3" |     |
| bool      | IS\\\_OPEN: "true" = open. "false" = closed.                                                                                                                                                      |     |


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ZONE_INFO", { ID = 2, NAME = "ENTRYWAY", TYPE_ID = 5, PARTITIONS = "1,3", IS_OPEN = true}, "NOTIFY")
```
