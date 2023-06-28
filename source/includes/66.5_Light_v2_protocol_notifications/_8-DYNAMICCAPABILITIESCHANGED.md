## DYNAMIC\_CAPABILITIES\_CHANGED

Used to update capabilities and proxy functionality without requiring a different c4i/c4z or for drivers that have capabilities that change during runtime.  Multiple parameters can be set with a single notify for 'atomic changes' where some functionality may involve mutual exclusion/inclusion.  

Example for parameters are `Notify("supports_broadcast_scenes=true","dimmer=true"`  


### Signature

`DYANAMIC_CAPABILITIES_CHANGED ()`


### Parameters

DYNAMIC\_CAPABILITIES\_CHANGED requires different parameters base on capability:

**Supports Zigbee Broadcast Scenes**

| Name | Value |
| --- | --- |
|supports\_broadcast\_scenes | true/false


**Level Target Support **

If the driver supports the new level target API: LIGHT\_BRIGHTNESS\_CHANGING and LIGHT\_BRIGHTNESS\_CHANGED. This provides better light level tracking for UI's, ALS Scenes, and Composer Programming interaction by allowing drivers to specify the current level, their target level and the number of milliseconds it will take for the light to reach the target level.  

| Name | Value |
| --- | --- |
| supports\_target | true/false |


**Dimmer**

Used to change if a light is a dimmer or switch at any time. This is very useful for having a single driver provide both functionality depending on what hardware is connected or detected.  Can also provide a dealer the ability to make a dimmer act as a switch for UI's and system functionality.

| Name | Value |
| --- | --- |
| dimmer | true/false |

Note: If true, updates the following feature capabilities:

- Reads ramp\_level from c4i, if not defined, false is assumed.
- Reads click/hold rates from c4i, if these are not defined, 0 is assumed.

Drivers using dynamic capabilities for ramp\_level, click, and hold rate settings should re-send dynamic capability notifies for each of these after setting dimmer to true.

If false - Sets the following:
- dimmer = false
- ramp\_level = false
- click/rates = 0


**Supports Brightness Stop**

| Name | Value |
| --- | --- |
| dimmer | true/false |
| supports\_brightness\_stop | true/false |


**Ramp Level **

| Name | Value |
| --- | --- |
| ramp\_level | true/false |


**Default Brightness Rate Min**

| Name | Value |
| --- | --- |
| brightness\_rate\_min | 0-INT16\_MAX |


**Default Brightness Rate Max**

| Name | Value |
| --- | --- |
| brightness\_rate\_max | 0-INT16\_MAX |


**Supports Color**

| Name | Value |
| --- | --- |
| supports\_color | true/false |


**Supports Color Correlated Temperature **

| Name | Value |
| --- | --- | 
| supports\_color\_correlated\_temperature | true/false |


**Color Temperature Correlated Min** 

What is the lowest supported CCT value. Must be increment of 10. Set both min/max to the same value if the CCT value can not be changed.

| Name | Value |
| --- | --- |
| color\_correlated\_temperature\_min | 500-20000 |


**Color Temperature Correlated Max** 

What is the highest supported CCT value. Must be increment of 10. Set both min/max to the same value if the CCT value can not be changed.

| Name | Value |
| --- | --- |
| color\_correlated\_temperature\_max | 500-20000 |


**Supports Color Stop**

| Name | Value |
| --- | --- |
| supports\_color\_stop | true/false |


**Color Rate Behavior**

| Name | Value |
| --- | --- |
| color\_rate\_behavior | Value. Values include: 0 - Unchangeable Rate, 1 - Device only supports one rate for brightness and color, 2 - Device supports ramping brightness and color at two different rates.|


**Default Color Rate Min**

| Name | Value |
| --- | --- |
| color\_rate\_min | 0-INT16\_MAX|


**Default Color Rate Max**

| Name | Value |
| --- | --- |
| color\_rate\_max | 0-INT16\_MAX |


**Color Trace Tolerance**

| Name | Value |
| --- | --- |
|color\_trace\_tolerance | 0-20 \* See capability documentation for more information.|


**Has Extras**

| Name | Value |
| --- | --- |
| has\_extras | true/false |


### Returns

`None`