
The following Conditionals are supported with the Security System Controller Partition. System programming conditionals are handled by the proxy and return a true or false:

`CURRENT_ARM_STATUS`

| Parameter | Description |
| --- | --- |
| == | equal |
| != | not equal |
| ARM STATE | One of the possible arm states listed in the `arm_states` configuration entry. These values are defined in the partition driver’s capabilities XML. See [arm_states][1] for more information.

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

`PREVIOUS_ARM_STATUS`
Same as `CURRENT_ARM_STATUS` but used to compares with the arm status before the last state change.

| Parameter | Description |
| --- | --- |
| == | equal |
| != | not equal |
| ARM STATE | One of the possible arm states listed in the `arm_states` configuration entry. These values are defined in the partition driver’s capabilities XML. See [arm_states][2] for more information._|

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#security-partition-capabilities
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#security-partition-capabilities