## SCHEDULE\_ENTRY\_CHANGED

Notification that should be sent to the proxy when a change is made to the HVAC schedules. Every entry that is changed will send one protocol notification.

 
### Name

`SCHEDULE_ENTRY_CHANGED ()` 


| Parameter     | Type | Description                                                                                |
| ------------- | ---- | ------------------------------------------------------------------------------------------ |
| DayIndex      | NUM  | Number representing day of week: 0= Sunday, 1=Monday                                       |
| EntryIndex    | NUM  | 0 to the number of entries the day can support. 0 = the first entry, 1 = the second entry. |
| TimeMinutes   | NUM  | Number of minutes past midnight for the entry change.  For example 360= 6:00AM.            |
| EnabledFlag   | BOOL | Enables or disables a schedule. By default, the first four schedules are enabled.          |
| HeatSetpoint  | NUM  | Temperature designated to start the heating system.                                        |
| CoolSetpoint: | NUM  | Temperature designated to start the cooling system.                                        |
| Units         | STR  | F or C – Fahrenheit or Celsius.                                                            |

 

### Returns

`None`

