## GET\_SETUP

Command handled by the proxy driver.  Immediately returns a block of XML information to the caller. Usually called just once by a UI entity to know how to setup the UI. This would report such things as how many settings the device has and what the name of those settings are.


### Name

`GET_SETUP ()`


### Parameters

`None`


### Returns

`None`


### Example

```xml
<fan_setup>
   <speeds_count>4</speeds_count>
   <speed_names>Low,Low Medium,Medium High,High</speed_names>
   <can_reverse>false</can_reverse>
   <can_set_preset>true</can_set_preset>
   <preset_speed>3</preset_speed>
</fan_setup>
```
