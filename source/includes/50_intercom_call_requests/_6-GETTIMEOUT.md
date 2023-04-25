## GET TIMEOUT

This request is issued to obtain the current timeout setting for manually answering a call.  If the timeout duration expires before a call is answered, the call is automatically ended.  This value is configured in the Video Intercom Agent in Composer.


### Signature

`GET_TIMEOUT ()`


### Parameter

`None`


### Response Parameters

| Parameter | Description |
| --- | --- |
| num | The duration (in seconds) for how long a new call should wait without being answered before the call is ended (number from 10 to 120). |


Response Prototype

```lua
<timeout>
  <value>[integer value]</value>
</timeout>
```

