## LOCK CAPABILITIES


The following Capabilities are supported with the Lock Proxy. Note that these capabilities will persist their values. This can result in inaccurate capability values being displayed on Navigators. 

The correct way to update these capabilities when a driver is updated is with the [DYNAMIC\_CAPABILITY\_CHANGED][1] notification. For example see the lua code to the right which uses name/value pairs:


```xml
C4:SendToProxy(5001, 'CAPABILITY_CHANGED', { NAME = 'shutout_timer_values', VALUE = '10, 30' } , 'NOTIFY')
 
C4:SendToProxy(5001, 'CAPABILITY_CHANGED', { NAME = 'shutout_timer_display_values', VALUE = '10s, 30s' }, 'NOTIFY') 
```


### Capabilities

`<auto_lock_time_display_values></auto_lock_time_display_values>`

Comma delimited list of correlating display values: str


`<auto_lock_time_values></auto_lock_time_values>`

 Comma delimited list of increasing values: int


`<has_admin_code></has_admin_code>`

Defines whether the lock has an admin code that must be entered to access lock management.  true|false 


`<has_auto_lock_time></has_auto_lock_time>`

Defines whether a lock has an auto lock setting. A lock can auto lock after a set amount of time or not auto lock if time set to 0 – OFF: true|false


`<has_custom_settings></has_custom_settings>`

Defines whether the lock supports any custom settings that should be added to the list of standard proxy defined settings. See `lock_custom_settings` data-to-ui:  true|false 


`<has_date_range_schedule></has_date_range_schedule>`

Defines whether the lock supports a date range schedule for users:  true|false 


`<has_daily_schedule></has_daily_schedule>`

Defines whether the lock supports a daily schedule for users:  true|false 


`<has_internal_history></has_internal_history>`

Defines whether the lock maintains its own list of log / history items:  true|false
 

`<has_language></has_language>`

Defines whether the lock has a setting for different languages:  true|false
 

`<has_log_item_count></has_log_item_count>`

Defines whether a lock has a setting for the number of log items to store for internal logging/history:  true|false
 

`<has_log_failed_attempts></has_log_failed_attempts>`

Defines whether a lock has a setting for logging failed keypad unlock attempts:  true|false
 

`<has_lock_modes></has_lock_modes>`

Defines whether the lock has a setting for different modes. Vacation mode prevents users from opening a lock using the keypad. Privacy mode prevents users from opening a lock using the keypad. However, if a key is used during privacy mode the lock resets to normal mode. Not all modes have to be supported.  true|false 


`<has_one_touch_locking></has_one_touch_locking>`

Defines whether the lock has a setting to allow one touch locking at the keypad without entering full key code:  true|false
 

`<has_schedule_lockout></has_schedule_lockout>`

Defines whether a lock has a schedule lockout setting. The schedule lockout can be used to prevent all users from manually unlocking a lock using the lock's keypad. This is similar to privacy mode:  true|false
 

`<has_settings></has_settings>`

Defines whether the lock supports any settings:  true|false 


`<has_shutout_timer></has_shutout_timer>`

Defines whether the lock has a setting for how long to disable lock keypad after failed attempts:  true|false 


`<has_volume></has_volume>`

Defines whether the lock has a setting for volume:  true|false 


`<has_wrong_code_attempts</has_wrong_code_attempts>`

Defines whether the lock has a setting for the number of failed unlock attempts to allow before temporarily disabling the lock: true|false 


`<is_management_only></is_management_only>`

Defines whether the lock is only used for managing users A lock that is management only does not support the LOCK, UNLOCK, and TOGGLE commands:  true|false 


`<language_values></language_values>`

English, French, Spanish …:  str


`<lock_modes_values></lock_modes_values>`

normal, vacation, privacy: str


`<log_item_count_values></log_item_count_values>`

Comma delimited list of increasing values: int 


`<max_users></max_users>`

The maximum number of user that can be added to a lock: int


`<shutout_timer_display_values></shutout_timer_display_values>`

 Comma delimited list of correlating display values: str


`<shutout_timer_values></shutout_timer_values>`

Comma delimited list of increasing values: int


`<wrong_code_attempts_values> </wrong_code_attempts_values>`

 Comma delimited list of increasing values: int


[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#dynamic-capability-changed