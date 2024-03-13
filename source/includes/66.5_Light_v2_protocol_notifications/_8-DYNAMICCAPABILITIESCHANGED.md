## DYNAMIC\_CAPABILITIES\_CHANGED

Used to update capabilities and proxy functionality without requiring a different c4i/c4z or for drivers that have capabilities that change during runtime.  Multiple parameters can be set with a single notify for 'atomic changes' where some functionality may involve mutual exclusion/inclusion.  

Example for parameters are `Notify("supports_broadcast_scenes=true","dimmer=true"`  


### Name

`DYANAMIC_CAPABILITIES_CHANGED ()`


### Parameters

DYNAMIC\_CAPABILITIES\_CHANGED requires different parameters base on capability:

**Supports Zigbee Broadcast Scenes**

| Parameter                 | Type | Description                      |
| ------------------------- | ---- | -------------------------------- |
| supports broadcast scenes | BOOL | Supports Zigbee Broadcast Scenes |


**Level Target Support **

If the driver supports the new level target API: LIGHT\_BRIGHTNESS\_CHANGING and LIGHT\_BRIGHTNESS\_CHANGED. This provides better light level tracking for UI's, ALS Scenes, and Composer Programming interaction by allowing drivers to specify the current level, their target level and the number of milliseconds it will take for the light to reach the target level.  

| Parameter       | Type | Description                       |
| --------------- | ---- | --------------------------------- |
| supports target | BOOL | Supports the new level target API |


**Dimmer**

Used to change if a light is a dimmer or switch at any time. This is very useful for having a single driver provide both functionality depending on what hardware is connected or detected.  Can also provide a dealer the ability to make a dimmer act as a switch for UI's and system functionality.

| Parameter | Type | Description                                   |
| --------- | ---- | --------------------------------------------- |
| dimmer    | BOOL | If a light is a dimmer or switch at any time. |

Note: If true, updates the following feature capabilities:

- Reads ramp\_level from c4i, if not defined, false is assumed.
- Reads click/hold rates from c4i, if these are not defined, 0 is assumed.

Drivers using dynamic capabilities for ramp\_level, click, and hold rate settings should re-send dynamic capability notifies for each of these after setting dimmer to true.

If false - Sets the following:
- dimmer = false
- ramp\_level = false
- click/rates = 0


**Supports Brightness Stop**

| Parameter                | Type       | Description |
| ------------------------ | ---------- | ----------- |
| dimmer                   | BOOL       |             |
| supports brightness stop | true/false |             |


**Ramp Level **

| Parameter  | Type | Description        |
| ---------- | ---- | ------------------ |
| ramp level | BOOL | Support ramp level |


**Default Brightness Rate Min**

| Parameter           | Type | Description |
| ------------------- | ---- | ----------- |
| brightness rate min | INT  | 0-INT16 MAX |


**Default Brightness Rate Max**

| Parameter           | Type | Description |
| ------------------- | ---- | ----------- |
| brightness rate max | INT  | 0-INT16 MAX |


**Supports Color**

| Parameter      | Type | Description    |
| -------------- | ---- | -------------- |
| supports color | BOOL | Supports color |


**Supports Color Correlated Temperature **

| Parameter                             | Type       | Description                           |
| ------------------------------------- | ---------- | ------------------------------------- |
| supports color correlated temperature | true/false | Supports color correlated temperature |


**Color Temperature Correlated Min** 

What is the lowest supported CCT value. Must be increment of 10. Set both min/max to the same value if the CCT value can not be changed.

| Parameter                        | Type      | Description                |
| -------------------------------- | --------- | -------------------------- |
| color correlated temperature min | 500-20000 | Lowest supported CCT value |


**Color Temperature Correlated Max** 

What is the highest supported CCT value. Must be increment of 10. Set both min/max to the same value if the CCT value can not be changed.

| Parameter                        | Type      | Description                 |
| -------------------------------- | --------- | --------------------------- |
| color correlated temperature max | 500-20000 | Highest supported CCT value |


**Supports Color Stop**

| Parameter           | Type | Description         |
| ------------------- | ---- | ------------------- |
| supports color stop | BOOL | Supports color stop |


**Color Rate Behavior**

| Parameter           | Type                                                                                                                                                                               | Description         |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| color rate behavior | Value. Values include: 0 - Unchangeable Rate, 1 - Device only supports one rate for brightness and color, 2 - Device supports ramping brightness and color at two different rates. | Color Rate Behavior |


**Default Color Rate Min**

| Parameter      | Type | Description |
| -------------- | ---- | ----------- |
| color rate min | INT  | 0-INT16 MAX |


**Default Color Rate Max**

| Parameter      | Type | Description |
| -------------- | ---- | ----------- |
| color rate max | 0INT | 0-INT16 MAX |


**Color Trace Tolerance**

| Parameter             | Type | Description                                               |
| --------------------- | ---- | --------------------------------------------------------- |
| color trace tolerance | NUM  | 0-20 * See capability documentation for more information. |


**Has Extras**

| Parameter  | Type | Description |
| ---------- | ---- | ----------- |
| has extras | BOOL |             |


### Returns

`None`