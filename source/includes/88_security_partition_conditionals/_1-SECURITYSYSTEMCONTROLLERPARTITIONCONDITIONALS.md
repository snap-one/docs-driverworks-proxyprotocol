
The following Conditionals are supported with the Security System Controller Partition. System programming conditionals are handled by the proxy and return a true or false:


`IS_ALARM`
Return true if the current state is ALARM.

`IS_ARMED`
Return true if the current state is ARMED, ENTRY DELAY, EXIT DELAY or ALARM

`IS_AWAY`
Return true if the partition is armed for away. Will be deprecated.

`IS_DISARMED`
Return true if the partition is disarmed (states DISARMED READY or DISARMED NOT READY).

`IS_HOME`
Return true if the partition is armed for home. Will be deprecated.

`IS_IN_ENTRY_DELAY`
Return true if the current state is ENTRY DELAY

`IS_IN_EXIT_DELAY`
Return true if the current state is EXIT DELAY