## SET CAMERA ENABLE

This command is issued to enable or disable the camera on an intercom device.


### Signature

`C4: SET_CAMERA_ENABLE  ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating whether enable or disable the camera on an intercom device. Enabled = 1, true, yes or on.  Disabled = 0, false, no or off. |


### Returns

`None`


### Example

```lua
<SET_CAMERA_ENABLED>
    <cameraEnable>[true]</cameraEnabled>
</SET_CAMERA_ENABLED>
```
