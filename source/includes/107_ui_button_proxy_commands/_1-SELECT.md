## SELECT

This command comes from the UI when a user selects the shortcut for the button. It is passed to the protocol driver and also sends the Selected event.


### Signature

`SELECT`


| Parameter | Description |
| --- | --- |
| Device ID | num: The room device ID value where the shortcut was pressed in. Exposed by the `LAST_ROOM_SELECTED` variable.
| Menu | str: The name of the menu the shortcut was selected in. Possible values: "listen", "watch", "security", "comfort", "service". Exposed by the `LAST_MENU_SELECTED` variable.




