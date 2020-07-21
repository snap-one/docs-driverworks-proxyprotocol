## SECURITY SYSTEM CONTROLLER PARTITION VARIABLES

The Security System Controller Partition supports the following Variables:

`HOME_STATE` Boolean. True when armed home. Will be deprecated.

`AWAY_STATE` Boolean. True when armed away. Will be deprecated.

`DISARMED_STATE` Boolean. True when disarmed. Will be deprecated.

`ALARM_STATE` Boolean. True when in an alarm state.

`DISPLAY_TEXT` String. Current text in the display window.

`TROUBLE_TEXT` String. Current text in the trouble window. When trouble text is blank, the UI will hide the trouble text window and give the space to the display text window.

`IS_ACTIVE` Boolean. True if this partition is active and can be used.

`PARTITION_STATE` String. Text representation of the current state.

`DELAY_TIME_TOTAL` Integer. The total length of the current Entry or Exit delay. If not in a delay, this will be 0.

`DELAY_TIME_REMAINING` Integer. The amount of time remaining in the current Entry or Exit delay. If not in a delay this will be 0.

`OPEN_ZONE_COUNT` Integer. The number of zones in this partition which are currently open.  Usually this will only matter when the armed state is `DISARMED_NOT_READY`.

`ALARM_TYPE` String. If the system is currently in the ALARM state, this will be a string representation of the type of alarm (Burglary, Fire, Medical, Panic, Carbon Monoxide, etc.).

`ARMED_TYPE` String. If we the system is currently in the ARMED state, this will be a string representation of type of arming (HOME, AWAY, etc.).

`LAST_EMERGENCY` String. When an emergency is triggered, this variable will store which type of emergency it was.  e.g. “Police” or “Panic.