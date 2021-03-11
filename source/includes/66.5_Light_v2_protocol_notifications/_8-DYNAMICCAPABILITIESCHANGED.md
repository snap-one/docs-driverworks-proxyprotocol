## DYNAMIC CAPABILITIES CHANGED

Used to update capabilities and proxy functionality without requiring a different c4i/c4z file.  Also used  for drivers that have capabilities that change during runtime.  Multiple parameters can be set with a single notify for 'atomic changes' where some functionality may involve mutual exclusion/inclusion.  

### Signature

`DYANAMIC_CAPABILITIES_CHANGED ()`


### Parameters

If the device supports Zigbee Broadcast Scenes one parameter is required:

| Parameter | Description |
| --- | --- |
| bool | true/false |


If the device supports dimming, the following parameter can be used to change if a light is a dimmer or switch at any time. This is very useful for having a single driver provide both functionality depending on what hardware is connected or detected.  This can also provide a dealer the ability to make a dimmer act as a switch for UI's and system functionality.

| Parameter | Description |
| --- | --- |
| name | dimmer |
| bool | true/false |

An Example for these parameters would be:

`Notify("supports_broadcast_scenes=true","dimmer=true"`



### Returns

`None`