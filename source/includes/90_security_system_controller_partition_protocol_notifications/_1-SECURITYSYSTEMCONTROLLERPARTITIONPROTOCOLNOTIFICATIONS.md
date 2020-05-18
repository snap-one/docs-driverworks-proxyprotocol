## SECURITY SYSTEM CONTROLLER PARTITION PROTOCOL NOTIFICATIONS

The following Notifications are supported by the Security System Controller Partition:

### Usage Note

When specifying a parameters value that is a number with a decimal, the value must be sent as a String. For example, if PARAM=1.5, the proxy will get the value of 1 from the protocol driver. PARAM="1.5" will result in the proxy getting the value of 1.5. This applies for temperatures, setpoints, and all other parameters that are part of a Notify message.  If you hare using a lua variable that is a number, consider doing PARAM=""..num to force the parameter to be a string.


## ALARM\`
\`Set the alarm state to “ALARM” and fire event.



## ALARM CLEAR
Set the alarm state to “AlarmCleared” and fire event.



## ARM FAILED
Sent when the partition failed to arm.

| Parameter | Description |
| --- | --- |
| str | ACTION: Optional. One of the following: KEYPAD (if a keycode is needed), BYPASS (if a bypass is needed), or NA (general failure) |
| bool | INTERFACE ID | Unique identifier of the interface that attempted the arming command. |



## AWAY
Set the armed state to “Armed Away” and fire event.



## AWAY INIT
Set the armed state to “Armed Away” but don't fire any events.



## CLEAR ZONE LIST
Instructs the partition to clear its zone list. Assumes a new list will be forthcoming.



## CODE REQUIRED
Informs the partition tha ta use code is required (or not required) to arm it.

| Parameter | Description |
| --- | --- |
| bool |CODE REQUIRED TO ARM: Whether or not a user code is required to arm this partition. |



## DISARMED
Set the armed state to “Disarmed” and fire event.



## DISARM FAILED
Sent when the partition failed to disarm.

| Parameter | Description |
| --- | --- |	
| str | INTERFACE ID: Unique identifier of the interface that attempted the disarming command. |



## DISARMED INIT
Set the armed state to “Disarmed” but don't fire any events.



## DISPLAY TEXT
| Parameter | Description |
| --- | --- |
| str | DATA STRING: Text to Display Text to show in the window. The UI displays should have two lines to display. If text is desired to show up on the second line, the text (str) should have a newline character in it. |



## EMERGENCY TRIGGERED
Sent when an Emergency function was performed.

| Parameter | Description |
| --- | --- |
| str |TYPE: Which emergency was just triggered, e.g. “Medical” or “Police” |



## HAS ZONE
Informs the partition that this zone is one of its members.

| Parameter | Description |
| --- | --- |
| int | ZONE ID: Identifies the member zone. |



## HOME INIT
Set the armed state to “Armed Home” but don’t fire any events.



## HOME
Set the armed state to “Armed Home” and fire event.



## INTERFACE ID
A unique identifier string that identifies which the interfaces should respond.  Usually this would be the InterfaceID parameter from the last command. An empty string would mean that all the interfaces could or should respond to this request.

| Parameter | Description |
| --- | --- |
| str | PROMPT: This will be the string the UI will use as a prompt when asking for the additional information. |
| str | INFO STRING: This will be the string with the required information to use when we receive the `ADDITIONAL_INFO` command. |
| str | FUNCTION NAME: Optional. Defaults to “” Used along with `INFO_STRING` to give information to the protocol driver as to what function to call when the new information is returned. |
| bool | MASK DATA: Optional. Defaults to ‘false’ When ‘true’ the targeted UI should not display the actual characters entered. This could be used when the user is entering sensitive information such as a pass code. |



## PARTITION ENABLED
Specifies whether or not this partition is enabled.

| Parameter | Description |
| --- | --- |
| bool | ENABLED: True if the partition is now enabled. False if it is now disabled. |



## PARTITION STATE
Sent when partition state changes.

| Parameter | Description |
| --- | --- |
| str | STATE: Valid values: `DISARMED_READY, DISARMED_NOT_READY, EXIT_DELAY, ARMED, ENTRY_DELAY, ALARM` |
| str | TYPE: For use with the ARMED or ALARM states. Specifies the type of arming or alarm that the system is changing to. |
| int | DELAY TIME TOTAL: Optional. For use with the `ENTRY_DELAY` or `EXIT_DELAY` states.  The total number of seconds that the current delay will last. If this parameter isn't included, the proxy will assume a value of 0. |
| int | DELAY TIME REMAINING: Optional. For use with the `ENTRY_DELAY` or `EXIT_DELAY` states. The number of seconds remaining in the current delay. If this parameter isn't included, the proxy will assume a value of 0. |
| | CODE REQUIRED TO CLEAR - For use with the alarm state. Most alarms require a user code to dismiss so this should be set to true. If the state is being set to ALARM, but can be dismissed with just a button press, set to false. |



## PARTITION STATE INIT
Sent when partition state changes however no programming events will fire from this notification.

| Parameter | Description |
| --- | --- |
| str |STATE: Valid values: `DISARMED_READY, DISARMED_NOT_READY, EXIT_DELAY, ARMED, ENTRY_DELAY, ALARM` |



## REMOVE ZONE
Tells the partition that this zone is no longer one of its members.

| Parameter | Description |
| --- | --- |
| int | ZONE ID: Identifies the non-member zone. |



## REQUEST ADDITIONAL INFO
Tells the partition proxy to ask for more information from the UIs. Often this would be used if a user code or an installer code is required to complete a desired action.  The new information will come back to the protocol driver in the form of an `ADDITIONAL_INFO` command. The `ADDITIONAL_INFO` command will have as one of its parameters the `INFO _STRING` parameter that was send up with this command.  It is intended that this will contain enough information that the driver will know which action to retry. (See the `ADDITIONAL_INFO` command).

| Parameter | Description |
| --- | --- |
| str | INTERFACE ID:  A unique identifier (str) that identifies of the interfaces should respond. Usually this would be the InterfaceID parameter from the last command. An empty (str) would mean that all the interfaces could or should respond to this request |
| str | PROMPT:  This will be the (str) the UI will use as a prompt when asking for the additional information. |
| str | INFO STRING: This will be the (str) with the required information to use when we receive the `ADDITIONAL_INFO` command. |
| str | FUNCTION NAME: Optional. Defaults to “”Used along with `INFO _STRING`  to give information to the protocol driver as to  what function to call when the new information is returned. |
| bool | MASK DATA: Optional. Defaults to ‘false’ When ‘true’ the targeted UI should not display the actual characters entered. This could be used when the user is entering sensitive information such as a pass code. |



## TROUBLE
| Parameter | Description |
| --- | --- |
| str | DATA STRING: Display Text to show in the Trouble Text Window. |



## ZONE STATE
Sent when a zone changes state: open/close or (un)bypass

| Parameter | Description |
| --- | --- |
| INT | ZONE ID:  Identifies which zone has had the state change. The proxy may get notifications for zones that it doesn't include, but these can be ignored. |
| bool | ZONE OPEN:  True if the zone is open, false if it is closed. |
| bool | ZONE BYPASSED: True if the zone is currently bypassed, false if it is normal. |
