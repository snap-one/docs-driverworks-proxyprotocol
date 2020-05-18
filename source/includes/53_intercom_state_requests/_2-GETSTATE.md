## GET STATE

This request is issued to obtain the device state of a specified intercom endpoint. 


### Signature

`C4:GET_STATE ()`


### | Request Parameter | Description |
| --- | --- |
| idDevice | This request is issued to obtain the device state of a specified intercom endpoint. |



### Request Prototype

```lua
<GET_STATE>
   <idDevice>[17]</idDevice>
</GET_STATE>
```



### Response Parameters

| Parameter | Description |
| --- | --- |
| id | The proxy device id of the intercom endpoint to which this request’s response is sent. This value is used to insure that the response is processed by proper device driver (i.e. the requestor). It is a number that is greater than or equal to zero (0). |
| excludeFromNav | Boolean flag indicating the current state for this setting. (0=false, 1=true) |
| playDoorChime | Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| dndSetting |Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| autoAnswer | Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| currrentState | Numeric value indicating the current state of the device. (0=not ready, 1=idle, 2=busy, 3=max calls) |
| sendVideo | Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| monitorMode | Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| ringerVol | Numeric value indicating the current value of this setting. (0 to 100) |
| speakerVol | Numeric value indicating the current value of this setting. (0 to 100) |
| microphoneGain | Numeric value indicating the current value of this setting. (0 to 100) |
| showMainVideo | Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| showMirrorVideo | Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| cameraEnabled  |Boolean flag indicating the current value of this setting. (0=false, 1=true) |
| aecEnabled | Boolean flag indicating the current value of this setting. (0=false, 1=true) |



Response Prototype

```lua
<device_state proxyid=”[integer value]”>
   <excludeFromNav>[integer value]</excludeFromNav>
   <playDoorChime>[integer value]</playDoorChime>
   <dndSetting>[integer value]</dndSetting>
   <autoAnswer>[integer value]</autoAnswer>
   <currentState>[integer value]</currentState>
   <sendVideo>[integer value]</sendVideo>
   <monitorMode>[integer value]</monitorMode>
   <ringerVol>[integer value]</ringerVol>
   <speakerVol>[integer value]</speakerVol>
   <microphoneGain>[integer value]</microphoneGain>
   <showMainVideo>[integer value]</showMainVideo >
   <showMirrorVideo>[integer value]</showMirrorVideo >
   <cameraEnabled>[integer value]</cameraEnabled >
   <aecEnabled>[integer value]</aecEnabled >
</device_state> 
```

