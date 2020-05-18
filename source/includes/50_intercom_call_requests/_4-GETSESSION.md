## GET SESSION

This request is issued to obtain the active session information for the requesting device.


### Signature

`C4:GET_SESSION ()`


### Parameters

`None`


### Response Parameters

| Parameter | Description |
| --- | --- |
| ID | The proxy device id of the intercom endpoint to which this request’s response is sent.  This value is used to insure that the response is processed by proper device driver (i.e. the "requestor"). It is a number that is greater than or equal to zero (0). |
| sessionId | Numeric value indicating the session id for the active session. |
| videoMode |Numeric value indicating video mode being used for this session by the specified endpoint. (0=transmit/receive, 1=transmit only, 2=receive only, 3=no video) |
| audioMode | Numeric value indicating audio mode being used for this session by the specified endpoint. (0=transmit/receive, 1=transmit only, 2=receive only, 3=no audio) |
| callerName | The device name of the intercom endpoint which initiated the call. |
| callerDevId | The proxy device id of the intercom endpoint which initiated the call. |
| calleeDevId | The proxy device id of the intercom endpoint which received the call. |
| calleName |The device name of the intercom endpoint which received the call. |


Response Prototype

```lua
<device_session id=”[integer value]”>
   <sessionId>[integer value]</sessionId>
   <videoMode>[integer value]</videoMode>
   <audioMode>[integer value]</audioMode>
   <callerDevId>[integer value]</callerDevId>
   <callerName>[string value]</callerName>
   <calleeDevId>[integer value]</calleeDevId>
   <calleeName>[string value]</calleeName>
</device_session>
```
