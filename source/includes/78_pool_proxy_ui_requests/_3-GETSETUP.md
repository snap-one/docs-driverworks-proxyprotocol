## GET SETUP

Obtains the driver’s setup information.

### Example

```xml
pool_setup>
    <temp_min>34</temp_min>
    <temp_max>104</temp_max>
    <pool_pumpmodes>Off,On</pool_pumpmodes>
    <spa_pumpmodes>Off,On</spa_pumpmodes>
    <max_aux>15</max_aux>
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
            <items>Off,Alpine White,Sky Blue,Cobalt Blue,Caribbean Blue,Spring Green,Emerald Green,Emerald Rose,Magenta,Garnet Red,Violet,Color Splash</			items>
        </aux_type>
        <aux_type>
            <type>LIST</type>
            <provides_selected_item>false</provides_selected_item>
            <name>Light Dimmer Pentair</name>
            <items>Off,White,Light Green,Green,Cyan,Blue,Lavender,Magenta,Light Magenta,Color Splash</items>
        </aux_type>
        <aux_type>
            <type>LIST</type>
            <provides_selected_item>false</provides_selected_item>
            <name>Light Dimmer Hayward Color Logic</name>
            <items>Off,Voodoo Lounge,Deep Blue Sea,Afternoon Skies,Emerald,Sangria,Cloud White,Twilight,Tranquility,Gemstone,USA,Mardi Gras,Cool Cabaret</			items>
        </aux_type>
        <aux_type>
            <type>LIST</type>
            <provides_selected_item>false</provides_selected_item>
            <name>Light Dimmer Jandy LED Water Colors</name>
            <items>Off,Alpine White,Sky Blue,Cobalt Blue,Caribbean Blue,Spring Green,Emerald Green,Emerald Rose,Magenta,Violet,Slow Color Splash,Fast 		Color Splash,USA,Fat Tuesday,Disco Tech</items>
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
</pool_setup>
```
