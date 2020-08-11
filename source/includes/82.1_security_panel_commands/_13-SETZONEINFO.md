## SET\_ZONE\_INFO

Set the information about a specified zone in the driver.

| Parameter | Description |
| --- | --- |
| int | ZONE\_ID: The id of the targeted zone. |
| str | NAME: The name by which we will now refer to this zone. |
| str | TYPE\_ID: The type of zone that the Control4 project will consider this zone. This will determine which icons will show up when it is referenced.  Valid values are:
| |”CONTACT\_SENSOR" 
| | ”EXTERIOR\_DOOR" |
| | “EXTERIOR\_WINDOW" |
| | “INTERIOR\_DOOR"  | 
| | "MOTION\_SENSOR" |
| | "FIRE" |
| | "GAS" |
| | "CARBON\_MONOXIDE" |
| | "HEAT" |
| | "WATER" |
| | "SMOKE" |
| | "PRESSURE" |
| | "GLASS\_BREAK" |
| | "GATE" |
| | "GARAGE\_DOOR"  |
| bool | DATA\_GUARDED: ‘True’ if these new settings should be protected so that information from the panel doesn’t overwrite them. |
| str | INTERFACE\_ID: Unique string ID indicating from where the command originated. |
