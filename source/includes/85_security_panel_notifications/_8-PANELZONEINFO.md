## PANEL\_ZONE\_INFO

Information about a given zone that Navigator or Composer can display.  


### Signature

`PANEL_ZONE_INFO ()`


| Parameter | Description |
| --- | --- |
| num | ID: ID of the target zone. |
| str | NAME: The zone's name either read from the panel or assigned by the user. Will default to "Zone NN"  |
| num | TYPE\_ID: The type of zone so that the Control4 system can map its sensor binding to a type of sensor. Current valid types with their ids are: | \_
| | UNKNOWN	= 0 |
| | CONTACT\_SENSOR= 1 |\_
| | EXTERIOR\_DOOR= 2 |\_
| | EXTERIOR\_WINDOW= 3 | \_
| | INTERIOR\_DOOR	= 4 | \_
| | MOTION\_SENSOR = 5 | \_
| | FIRE = 6 | 
| | GAS = 7 |
| | CARBON\_MONOXIDE	= 8 | \_
| | HEAT = 9 |
| | WATER = 10 |
| | SMOKE = 11 | 
| | PRESSURE = 12 | 
| | GLASS\_BREAK= 13 |
| | GATE = 14 |
| | GARAGE\_DOOR = 15 | \_
| str | PARTITIONS: Comma-delimited string of numbers indicating which partitions this zone is a  member of.  For example, if this zone is included in both partitions 1 and 3, the string would be "1,3" | 
| bool | IS\_OPEN: "true" = open. "false" = closed. |\_


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "PANEL_ZONE_INFO", { ID = 2, NAME = "ENTRYWAY", TYPE_ID = 5, PARTITIONS = "1,3", IS_OPEN = true} "NOTIFY")
```
