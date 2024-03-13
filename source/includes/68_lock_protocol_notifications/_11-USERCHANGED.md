## USER\_CHANGED

Sent when a user setting is changed.


### Name

`USER_CHANGED ()`


| Parameter | Description                                                                                                               |                                                                                                                                                                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| int       | USER ID                                                                                                                   |                                                                                                                                                                                                                  |
| str       | USER NAME                                                                                                                 |                                                                                                                                                                                                                  |
| str       | PASSCODE                                                                                                                  |                                                                                                                                                                                                                  |
| bool      | IS ACTIVE: Optional, true                                                                                                 | false. A user can be enabled or disabled without affecting schedule. Defaults to true.                                                                                                                           |
| bool      | SCHEDULED DAYS: Comma delimited BOOLEAN. Optional. Sunday – Saturday, true                                                | false. Defaults all true.                                                                                                                                                                                        |
| int       | START DAY:  1-31.                                                                                                         |                                                                                                                                                                                                                  |
| int       | START MONTH: 1-12.                                                                                                        |                                                                                                                                                                                                                  |
| int       | START YEAR:  YYYY.                                                                                                        |                                                                                                                                                                                                                  |
| int       | END DAY: 1-31                                                                                                             |                                                                                                                                                                                                                  |
| int       | END MONTH:  1-12.                                                                                                         |                                                                                                                                                                                                                  |
| int       | END YEAR:  YYYY.                                                                                                          |                                                                                                                                                                                                                  |
| int       | START TIME:  optional, minutes from midnight.                                                                             |                                                                                                                                                                                                                  |
| int       | END TIME: optional, minutes from midnight.                                                                                |                                                                                                                                                                                                                  |
| str       | SCHEDULE TYPE: Optional. daily                                                                                            | date range. A daily schedule will specify `SCHEDULED_DAYS`. A `date_range` will specify a start date and an end date. Both schedule types may be restricted to a `START_TIME` and `END_TIME`. Defaults to daily. |
| bool      | IS RESTRICTED SCHEDULE: Optional, true/false. Specifies whether or not to enforce the user’s schedule. Defaults to false. |                                                                                                                                                                                                                  |


### Returns

`None`
