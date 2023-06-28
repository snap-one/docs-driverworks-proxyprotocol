## EXTRAS\_SETUP\_CHANGED

Update the Extras Setup, displayed in the UI 

### Signature

`EXTRAS_SETUP_CHANGED ()`


| Parameter | Description |
| --- | --- |
| XML | XML text string of XML matching the Preset Schedule schema. Comes through to the UI as `extras_setup`. Note that as of OS 3, sending only a singular XML string is supported. For example, sending an array of Extras can result in Navigator performance issues. |


### Returns

`None`

