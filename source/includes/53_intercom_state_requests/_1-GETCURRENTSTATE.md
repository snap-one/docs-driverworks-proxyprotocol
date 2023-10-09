## GET\_CURRENT\_STATE

This request is issued to obtain the current device state of the intercom endpoint making the request. Upon receiving the request, the driver should issue a [CURRENT\_STATE\_CHANGED][1] notify.     


### Signature

`GET_CURRENT_STATE ()`


### Request Parameters

`None`


### Response Parameters

| Parameter | Description                                                                                                                                                                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id        | The proxy device id of the intercom endpoint to which this request’s response is sent. This value is used to insure that the response is processed by proper device driver (i.e. the requestor). It is a number that is greater than or equal to zero (0). |
| num       | Numeric value indicating the current state of the device. (0=not ready, 1=idle, 2=busy, 3=max calls)                                                                                                                                                       |


Response Prototype

```lua
<device_state proxyid=”[10]”>
   <currentState>[2]</currentState>
</device_state>
```

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-state-notifications-current_state_changed