# Light V2 Variables


**Light State:**
ID = 1000. Boolean indicating if the light Brightness is not at the Off preset. If you set this variable to true on a dimmer,  it will go to the On preset. On a switch, only the first variable exists. 



**Brightness Percent:**
ID = 1001.  An integer indicating the current brightness for a dimmer. The value should be between 0-100. 



**Brightness Target Ramp Rate in Milliseconds:** 
ID = 1120. Primarily for UI's who request brightness information during a ramp, as this will allow them to know how far through the ramp the light is. This is updated every 1000ms. This works for only drivers that have enabled the supports\_brightness\_target capability.



**Brightness Target Rate Remaining in Milliseconds:**
ID = 1121. Primarily for UI's who request brightness information during a ramp, as this will allow them to know how far through the ramp the light is. This is updated every 1000ms. This works for only drivers that have enabled the supports\_brightness\_target capability.



**Click Rate Up: **
ID = 1002. An integer indicating the number of milliseconds. (Used in "On" Preset).



**Click Rate Down:**
ID = 1003.  An integer indicating the number of milliseconds. (Used in "Off" Preset).



**Hold Rate Up:**
ID = 1004.  An integer indicating the number of milliseconds. (Used in "Slow On" Preset).



**Default On Preset Brightness:**
ID = 1006. An integer indicating what the preset "On" brightness is and thus what a light Brightness would go to if the top wall keypad button is clicked, regardless what the light level is at and including even if the current brightness is higher. (Used in "On" Preset).



**Max Brightness:**
ID = 1007. An integer indicating how high the light will go with a click. To go passed the max (still capped at 100%),  you need to press and hold.



**Min Brightness:**
ID = 1008. An integer on how low the light will go before skipping values between this number and 0/completely off. 



**Cold Start Brightness:**
ID = 1009. An integer of what level to go to when first turning on before attempting to do a ramp.
 


**Cold Start Time:**
ID = 1010. An integer indicating the amount of time in milliseconds to stay at the cold start level before starting a ramp. 



**Color Presets**
ID=1300. An XML string containing all of the Color Presets that are configured in the system. For UI use only.



**Color Active Presets**
ID=1301. An XML string containing all of the presets that are currently active. For UI use only.

 **See example to the right.**

```xml
<active_presets>
   <preset>
      <name>Relax</name>
      <id>2</id>
      <origin>2</origin>
   </preset>
</active_presets>
```

In the example to the right, the origin value indicates if the preset came from a device (1), or the color agent (2).



**Light Dynamic Capabilities**
ID=6661. An XML string containing the active dynamic capabilities for this light proxy. For UI use Only.


** See example to the right.**

```xml
<DynamicCapabilities>
  <supports_broadcast_scenes>False</supports_broadcast_scenes>
  <dimmer>False</dimmer>
  <supports_target>False</supports_target>
  <supports_color>False</supports_color>
  <supports_color_correlated_temperature>False<supports_color_correlated_temperature>
  <color_correlated_temperature_min>1000<color_correlated_temperature_min>
  <color_correlated_temperature_max>20000</color_correlated_temperature_max>
  <color_rate_behavior>0</color_rate_behavior>
  <color_rate_min>0</color_rate_min>
  <color_rate_max>0</color_rate_max>
  <color_trace_tolerance>2</color_trace_tolerance>
  <has_extras>False</has_extras>
  <click_rate_min>0</click_rate_min>
  <click_rate_max>86400000</click_rate_max>
  <hold_rate_min>1000</hold_rate_min>
  <hold_rate_max>86400000</hold_rate_max>
</DynamicCapabilities>
```


**VAR\_C4\_NESTING\_PARENTS\_CHILD\_DEVICES**
Set this variable to a comma delimited list of ID values for the secondary device(s) required by the parent driver. This list represents the drivers that will be nested under the parent driver in Composer Pro. This is the associated driver(s) with the nested\_driver\_is\_child capability set to true.


**VAR\_C4\_NESTED\_CHILDS\_PARENT\_DEVICE** 
Set the variable to the ID of primary driver requiring its use. This is the associated driver with the nesting\_driver\_is\_parent capability set to true.