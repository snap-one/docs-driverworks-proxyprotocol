## CUSTOM\_FIELDS\_CHANGED

Update the template Custom Fields that UI's display for a new Preset Event.


### Signature

`CUSTOM FIELDS CHANGED ()`


| Parameter | Description |
| --- | --- |
| XML | Text string of XML matching the Preset Schedule schema. To UI comes through as `preset_custom_fields`.



### Returns

\`None
\`

### Example

```xml
<preset_custom_fields>
 <field id="TemperatureSensor" type="list" label="Temperature Sensor:" default="Primary: Built-In Sensor, Secondary: None">
   <list>
    <item text="Primary: Built In Sensor Alias" value="Primary: Built-In Sensor, Secondary: None"/>                    
    <item text="Primary: Wired Remote Sensor Alias, Secondary: None" value="Primary: Wired Remote Sensor, Secondary: None"/>
    <item text="Primary: Built In Sensor Alias, Secondary: Wired Remote Sensor Alias" value="Primary: Built-In Sensor, Secondary:           Wired Remote Sensor"/<item text="Primary: Wired Remote Sensor Alias, Secondary: Built In Sensor Alias" value="Primary: Wired           Remote Sensor, Secondary: Built-In Sensor"/>
   </list>
 </field>
</preset_custom_fields>
```
