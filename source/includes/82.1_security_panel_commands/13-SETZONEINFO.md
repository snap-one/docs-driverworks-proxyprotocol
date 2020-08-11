## SET_ZONE_INFO

Set the information about a specified zone in the driver.

| Parameter | Description |
| --- | --- |
| int | ZONE_ID: The id of the targeted zone. |
| str | NAME: The name by which we will now refer to this zone. |
| str | TYPE_ID: The type of zone that the Control4 project will consider this zone. This will determine which icons will show up when it is referenced.  Valid values are:
| |”CONTACT_SENSOR" 
| | ”EXTERIOR_DOOR" |
| | “EXTERIOR_WINDOW" |
| | “INTERIOR_DOOR"  | 
| | "MOTION_SENSOR" |
| | "FIRE" |
| | "GAS" |
| | "CARBON_MONOXIDE" |
| | "HEAT" |
| | "WATER" |
| | "SMOKE" |
| | "PRESSURE" |
| | "GLASS_BREAK" |
| | "GATE" |
| | "GARAGE_DOOR"  |
| bool | DATA_GUARDED: ‘True’ if these new settings should be protected so that information from the panel doesn’t overwrite them. |
| str | INTERFACE_ID: Unique string ID indicating from where the command originated. |
