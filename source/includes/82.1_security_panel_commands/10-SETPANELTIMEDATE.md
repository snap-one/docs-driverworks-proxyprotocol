## SET_PANEL_TIME_DATE

Set the current date and time on the panel. This command is only available if the ‘can_set_time’ capability is set to ‘true’.


| Parameter | Description |
| --- | --- |
| int | YEAR: The current year (4 digits) |
| int | MONTH: The current month (2 digits 01-12) |
| int | DAY: The current day of the month (2 digits 01-31) |
| int | HOUR: The current hour in 24-hour time (2 digits 00-23) |
| int | MINUTE: The current minute in the hour (2 digits 00-59) |
| int | SECOND: The current second in the minute (2 digits 00-59) |
| str | INTERFACE_ID: Unique string ID indicating from where the command originated. |
