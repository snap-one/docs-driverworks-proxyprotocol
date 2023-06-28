## GET\_DEVICE

This request is issued to obtain the device properties of a specified intercom endpoint.


### Signature

`GET_DEVICE ()`


| Parameter | Description |
| --- | --- |
| num | The Proxy Device ID of the intercom endpoint whose custom button information is to be returned. |


### Example

```lua
<GET_DEVICE>
  <idDevice>[integer value]</idDevice>
</GET_DEVICE>
```

### Response Parameters

| Parameter | Description |
| --- | --- |
| proxyid | The proxy device id of the intercom endpoint for which the data was requested.  It is a number that is greater than or equal to zero (0) |
| protocolid | The protocol device id of the intercom endpoint for which the data was requested. It is a number that is greater than or equal to zero (0). |
| hasCamera | A Boolean flag indicating whether or not the indicated intercom device has a camera. (0=false, 1=true) |
| hasDisplay | A Boolean flag indicating whether or not the specified intercom endpoint has a display. (0=false, 1=true) |
| isDoorStation | A Boolean flag indicating whether or not the indicated intercom device is a door station. (0=false, 1=true) |
| displayName | The display name to be used when referring to the specified intercom endpoint in the system’s user interface (UI). |
| sipUserName | The SIP user name for the specified intercom endpoint. |
| sipAOR | The SIP address of record for the specified intercom endpoint. This takes the form of “[sip user name]()@[sip server IP address]()”.


Response Prototype

```lua
<device_props id=”[integer value]”>
    <proxyId>[integer value]</proxyId>
    <protocolId>[integer value]</protocolId>
    <hasCamera>[integer value]</hasCamera>
    <hasDisplay>[integer value]</hasDisplay>
    <hasButtons>[integer value]</hasButtons>
    <isDoorStation>[integer value]</isDoorStation>
    <displayName>[string value]</displayName>
    <sipUserName>[string value]</sipUserName>
    <sipAOR>[string value]</sipAOR>
</device_props>
```





