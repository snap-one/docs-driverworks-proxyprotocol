## SET\_PANEL\_TIME\_DATE

Set the current date and time on the panel. This command is only available if the ‘can\_set\_time’ capability is set to ‘true’.


| Parameter     | Type | Description                                                    |
| ------------- | ---- | -------------------------------------------------------------- |
| YEAR          | INT  | The current year (4 digits)                                    |
| MONTH         | INT  | The current month (2 digits 01-12)                             |
| DAY           | INT  | The current day of the month (2 digits 01-31)                  |
| HOUR:         | INT  | The current hour in 24-hour time (2 digits 00-23)              |
| MINUTE        | INT  | The current minute in the hour (2 digits 00-59)                |
| SECOND        | INT  | The current second in the minute (2 digits 00-59)              |
| INTERFACE ID: | STR  | Unique string ID indicating from where the command originated. |
