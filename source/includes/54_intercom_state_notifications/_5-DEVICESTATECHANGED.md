## DEVICE\_STATE\_CHANGED

This notification is issued by the protocol  when the endpoint’s current state has changed.

### Signature

`DEVICE_STATE__CHANGED ()`


| Parameter       | Description                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| excludeFromNav  | Boolean flag indicating the current state for this setting. (0=false, 1=true)                        |
| playDoorChime   | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| dndSetting      | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| autoAnswer      | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| currentState    | Numeric value indicating the current state of the device. (0=not ready, 1=idle, 2=busy, 3=max calls) |
| sendVideo       | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| monitorMode     | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| ringerVol       | Numeric value indicating the current value of this setting. (0 to 100)                               |
| speakerVol      | Numeric value indicating the current value of this setting. (0 to 100)                               |
| microphoneGain  | Numeric value indicating the current value of this setting. (0 to 100)                               |
| showMainVideo   | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| showMirrorVideo | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| cameraEnable    | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |
| aecEnabled      | Boolean flag indicating the current value of this setting. (0=false, 1=true)                         |


### Example

```lua
<DEVICE_STATE_CHANGED>
   <excludeFromNav>[1]</excludeFromNav>
   <playDoorChime>[0]</playDoorChime>
   <dndSetting>[0]</dndSetting>
   <autoAnswer>[0]</autoAnswer>
   <sendVideo>[1]</sendVideo>
   <currentState>[3]</currentState>
   <monitorMode>[1]</monitorMode>
   <ringerVol>[50]</ringerVol>
   <speakerVol>[70]</speakerVol>
   <microphoneGain>[35]</microphoneGain>
   <showMainVideo>[1]</showMainVideo>
   <showMirrorVideo>[1]</showMirrorVideo>
   <cameraEnabled>[0]</cameraEnabled>
   <aecEnabled>[1]</aecEnabled>
</DEVICE_STATE_CHANGED
```
