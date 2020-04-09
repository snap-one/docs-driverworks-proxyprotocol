## SETTINGS

Sent in response to the command `REQUEST_SETTINGS`.


### Signature

`C4:SETTINGS ()`


### Parameters

`None`


### Returns

`None`


### Example

```
<lock_settings>
	<admin_code> admin-code STRING </admin_code>
	<auto_lock_time> n INT </auto_lock_time>
	<log_item_count> n INT </log_item_count>
	<schedule_lockout_enabled> true | false </schedule_lockout_enabled>
	<lock_mode> normal | vacation | privacy </lock_mode>
	<log_failed_attempts> true | false </log_failed_attempts>
	<wrong_code_attempts> n INT </wrong_code_attempts>
	<shutout_timer> n INT </shutout_timer>
	<language> English | French | Spanish | etc. </language>
	<volume> silent | low | high </volume>
	<one_touch_locking> true | false </one_touch_locking>
</lock_settings>
```
