## POOL CAPABILITIES

The following Capabilities are supported with the Pool Proxy:

`<aux_types></aux_types>`
List of auxiliary types needed by the protocol driver. There are two types of auxiliary types supported: Toggle and List.


`<pool_heat_modes></pool_heat_modes>`
xml list of pool heat modes.


`<pool_pump_modes></pool_pump_modes>`
xml list of pool pump modes.


`<spa_heat_modes></spa_heat_modes>`
xml list of spa heat modes.


`<spa_ pump_modes></spa_ pump_modes>`
xml list of spa pump modes.


`<temp_max></temp_max>`
Should be entered as Fahrenheit value, it is automatically adjusted to Celsius when the pool is set to Celsius.


`<temp_min></temp_min>`
Should be entered as Fahrenheit value, it is automatically adjusted to Celsius when the pool is set to Celsius.


### Example

The example capabilities XML is from the Jandy Aqualink driver.

```xml
<capabilities>
         <pool_pumpmodes>Off,On</pool_pumpmodes>
         <spa_pumpmodes>Off,On</spa_pumpmodes>
         <temp_min>34</temp_min>
         <temp_max>104</temp_max>
         <pool_heat_modes>
               <mode>
                    <id>1</id>
                    <text>Heater</text>
                    <command>set_pool_heater</command>
               </mode>
               <mode>
                    <id>2</id>
                    <text>Solar Heater</text>
                    <command>set_solar_heater</command>
               </mode>
          </pool_heat_modes>
          <spa_heat_modes>
               <mode>
                    <id>1</id>
                    <text>Heater</text>
                    <command>set_spa_heater</command>
               </mode>
          </spa_heat_modes>
          <aux_types>
               <aux_type>
                    <type>TOGGLE</type>
                    <name>Toggle</name>
               </aux_type>
               <aux_type>
                    <type>LIST</type>
                    <provides_selected_item>false</provides_selected_item>
                    <name>Light Dimmer Jandy Colors</name>
                    <items>Off,Alpine White,Sky Blue,Cobalt Blue,Caribbean Blue,Spring Green,Emerald</items>
               </aux_type>
               <aux_type>
                    <type>LIST</type>
                    <provides_selected_item>false</provides_selected_item>
                    <name>Light Dimmer Pentair</name>
                    <items>Off,White,Light Green,Green,Cyan,Blue,Lavender,Magenta,Light Magenta,Color</items>
               </aux_type>
               <aux_type>
                    <type>LIST</type>
                    <provides_selected_item>false</provides_selected_item>
                    <name>Light Dimmer Hayward Color Logic</name>
                    <items>Off,Voodoo Lounge,Deep Blue Sea,Afternoon Skies,Emerald,Sangria,Cloud</items>
               </aux_type>
               <aux_type>
                    <type>LIST</type>
                    <provides_selected_item>false</provides_selected_item>
                    <name>Light Dimmer Jandy LED Water Colors</name>
                    <items>Off,Alpine White,Sky Blue,Cobalt Blue,Caribbean Blue,Spring Green</items>
               </aux_type>
               <aux_type>
                    <type>LIST</type>
                    <provides_selected_item>false</provides_selected_item>
                    <name>Light Dimmer Pentair Intellibright</name>
                    <items>Off,Sam,Party,Romance,Caribbean,American,California Sunset,Royal,Blue,Green,Red,White,Magenta</items>
               </aux_type>
               <aux_type>
                    <type>LIST</type>
                    <provides_selected_item>true</provides_selected_item>
                    <name>Dimmer</name>
                    <items>Off,25%,50%,75%,100%</items>
               </aux_type>
          </aux_types>
     </capabilities>
```
