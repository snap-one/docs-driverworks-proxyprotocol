PRESET FIELDS CHANGED

Updates the  Preset FIELDS TEMPLATE that UIs display for a Preset Event. To UI comes through as `preset_fields`.  Ifthis is modified, it is possible that existing presets will have data that is not in compliance. However, a protocol driver can modify this to have new `preset_fields` which are compatible. Do not delete this as Events are erased when presets are deleted. 



### Signature

`C4:PRESET_FIELDS_CHANGED ()` 


| Parameter | Description |
| --- | --- |
| XML | XML text string of XML matching the Preset Schedule schema |
 

### Returns

`None`

