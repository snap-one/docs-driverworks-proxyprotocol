## GET SESSION LIST

This request is issued to obtain the session information of all of sessions on this endpoint.


### Signature

`C4:GET_SESSION_LIST ()`


### Parameters

`None`


### Response Parameters

| Parameter | Description |
| --- | --- |
| `session_list` | A container for the collection of session information records. |
| `device_session` | A `device_props` record for each intercom endpoint in the project.  See the response format for the `GET_SESSION`. |


Response Prototype

```
<session_list>
  <device_session id=”Id1”>
   [see the GET_SESSION response format]
  </device_session>
  <device_session id=”Id2”>
   [see the GET_SESSION response format]
  </device_session>
  <device_session id=”IdN”>
   [see the GET_SESSION response format]
  </device_session>
</session_list>
```
