## SCHEDULE ENTRY CHANGED

Notification that should be sent to the proxy when a change is made to the HVAC schedules. Every entry that is changed will send one protocol notification.

 
### Signature

`C4:SCHEDULE_ENTRY_CHANGED ()` 


| Parameter | Description |
| --- | --- |
| num | DayIndex: Number representing day of week: 0= Sunday, 1=Monday |
| num | EntryIndex : 0 to the number of entries the day can support. 0 = the first entry, 1 = the second entry. |
| num | TimeMinutes: Number of minutes past midnight for the entry change.  For example 360= 6:00AM. |
| bool | EnabledFlag: Enables or disables a schedule. By default, the first four schedules are enabled. |
| num | HeatSetpoint: Temperature designated to start the heating system. |
| num | CoolSetpoint: Temperature designated to start the cooling system. |
| str | Units  (string): F or C – Fahrenheit or Celsius. |
 

### Returns

`None`

