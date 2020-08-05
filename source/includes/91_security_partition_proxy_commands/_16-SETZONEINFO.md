## SET ZONE INFO

Display the given string in the trouble text field.


| Parameter | Description |
| --- | --- |
| int | ID: ID of the targeted zone. |
| str | Name:  Name of this zone. |
| int | Type Id: Control4 Zone Type ID. |
| bool | Can Control: True if this zone has a relay associated with it. |
| bool | Can Bypass: True id this zone can be bypassed. |
| int | Room Id: Control4 device ID of the room that the sensor bound to this zone is located. |
| str | Room Name:  Name of the room that the sensor bound to this zone is located. "" if the zone is not bound to a sensor. |



### Returns

`None`
