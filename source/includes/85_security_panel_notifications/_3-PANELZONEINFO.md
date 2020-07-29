## PANEL_ZONE_INFO

Information about a given zone that Navigator or Composer can display.  


### Signature

`PANEL_ZONE_INFO ()`


| Parameter | Description |
| --- | --- |
| num | ID: ID of the target zone. |
| str | NAME: The zone's name either read from the panel or assigned by the user. Will default to "Zone NN"  |
| num | TYPE_ID: The type of zone so that the Control4 system can map its sensor binding to a type of sensor. Current valid types with their ids are: | _
| | UNKNOWN	= 0 |
| | CONTACT_SENSOR= 1 |_
| | EXTERIOR_DOOR= 2 |_
| | EXTERIOR_WINDOW= 3 | _
| | INTERIOR_DOOR	= 4 | _
| | MOTION_SENSOR = 5 | _
| | FIRE = 6 | 
| | GAS = 7 |
| | CARBON_MONOXIDE	= 8 | _
| | HEAT = 9 |
| | WATER = 10 |
| | SMOKE = 11 | 
| | PRESSURE = 12 | 
| | GLASS_BREAK= 13 |
| | GATE = 14 |
| | GARAGE_DOOR = 15 | _
| str | PARTITIONS: Comma-delimited string of numbers indicating which partitions this zone is a  member of.  For example, if this zone is included in both partitions 1 and 3, the string would be "1,3" | 
| bool | IS_OPEN: "true" = open. "false" = closed. |_


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ZONE_INFO", { ID = 2, NAME = "ENTRYWAY", TYPE_ID = 5, PARTITIONS = "1,3", IS_OPEN = true}, "NOTIFY")
```
