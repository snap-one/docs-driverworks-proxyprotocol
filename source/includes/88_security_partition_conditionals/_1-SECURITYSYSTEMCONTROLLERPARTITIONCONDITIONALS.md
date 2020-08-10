
The following Conditionals are supported with the Security System Controller Partition. System programming conditionals are handled by the proxy and return a true or false:

`CURRENT_ARM_STATUS`

| Parameter | Description |
| --- | --- |
| == | equal |
| != | not equal |
| ARM STATE | One of the possible arm states listed in the `arm_states` configuration entry. 

`IS_ALARM`
Returns true if the current state is ALARM.

`IS_ARMED`
Returns true if the current state is ARMED, ENTRY DELAY, EXIT DELAY or ALARM

`IS_AWAY`
Returns true if the partition is armed for away. Note this has been deprecated and is present for backwards compatibility purposes.

`IS_DISARMED`
Returns true if the partition is currently disarmed (states DISARMED READY or DISARMED NOT READY).

`IS_HOME`
Returns true if the partition is armed for home (states HOME or Stay). Note this has been deprecated and is present for backwards compatibility purposes.

`IS_IN_ENTRY_DELAY`
Returns true if the current state is ENTRY DELAY

`IS_IN_EXIT_DELAY`
Returns true if the current state is EXIT DELAY

`PREVIOUS\_ARM\_STATUS`
Same as `CURRENT\_ARM\_STATUS` but used to compares with the arm status before the last state change. 

| Parameter | Description |
| --- | --- |
| == | equal |
| != | not equal |
| ARM STATE | One of the possible arm states listed in the `arm_states` configuration entry. |
