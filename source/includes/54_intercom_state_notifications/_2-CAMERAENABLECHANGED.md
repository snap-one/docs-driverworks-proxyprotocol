## CAMERA\_ENABLED\_CHANGED

This notification is issued by the protocol when the endpoint’s Camera Enabled setting has changed.


### Signature

 `CAMERA_ENABLED_CHANGED ()`


| Parameter | Description                                                                                   |
| --------- | --------------------------------------------------------------------------------------------- |
| int       | The proxy device id of the intercom endpoint whose device state information is being returned |
| int       | cameraEnabled: Boolean flag indicating the current state for this setting. (0=false, 1=true)  |


### Example

```lua
<device_state id=[10]>
   <cameraEnabled>[1]</cameraEnabled>
</device_state>
```
