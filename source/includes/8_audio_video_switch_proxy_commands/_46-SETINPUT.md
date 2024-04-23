## SET\_INPUT

Specify input selection of device.


### Name

`SET_INPUT ()`

| Parameter         | Type | Description                                                                             |
| ----------------- | ---- | --------------------------------------------------------------------------------------- |
| Input Binding ID  | int  | Binding ID in the BindingID range below.                                                |
| PREV DEV LIST     | str  | Value of the device directly upstream in the AV path.                                   |
| Output Binding ID | int  | Optional. Output Binding ID - should be in the BindingID range in the usage note below. |


### Returns

`None`


### Usage Note

-  Control Bindings = 1 -\> 999
- Video Inputs = 1000 -\> 1099
- Video Outputs = 2000 -\> 2999
- Audio Inputs = 3000 -\> 3099
- Audio Outputs = 4000 -\> 4999
- Proxy Bindings = 5000 -\> 5999
- Network Bindings = 6000 -\> 6999
- Room Bindings = 7000 -\> 7999
- Power Manager = 8000 -\> 8999

