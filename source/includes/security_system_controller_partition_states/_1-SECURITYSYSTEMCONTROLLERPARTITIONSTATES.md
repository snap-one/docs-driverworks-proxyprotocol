## SECURITY SYSTEM CONTROLLER PARTITION STATES

The following States are supported by the Security System Controller Partition. These states were added to the Proxy in operating system release 2.9.0.

## ALARM
The partition is in an alarm state.  A separate variable will indicate which type of alarm (Burglary, Fire, CO, etc.).

## ARMED
The partition is armed. A separate variable would keep track of what type of armed state.  HOME and AWAY would be the most common types, but the protocol driver could specify other types if desired.

## CONFIRMATION REQUIRED
Some panels require an extra confirmation from the user after an alarm has been cleared before they will go back into `DISARMED_READY` state.  When in this state, the panel is waiting for a `SEND_CONFIRMATION` command from one of the UIs.

## DISARMED READY
The partition is disarmed, but could be armed if desired.

## DISARMED NOT READY
The partition is disarmed, but not ready to be armed; usually because one of its zones is currently open.

## EXIT DELAY
The user has given the arm command, but the partition is in the delay time which allows the user to exit the area before the alarm is tripped.

## ENTRY DELAY
The user has opened a zone while the partition is armed. He has a certain amount of time to disarm the system before the alarm engages.

## OFFLINE
The partition is in an OFFLINE state.