## GET DEVICE LIST

This request is issued to obtain the device properties of all of the intercom endpoints in the project.


### Signature

`C4:GET_DEVICE_LIST ()`


### Parameters

`None`


### Response Parameters

| Parameter | Description |
| --- | --- |
| `device_list` | A container for the collection of device property records. |
| `device_props` | A `device_props` record for each intercom endpoint in the project.  See the response format for the `GET_DEVICE`. |


Response Prototype

```
<device_list>
   <device_props id=”Id1”>
    [see the GET_DEVICE response format]
   </device_props>
   <device_props id=”Id2”>
    [see the GET_DEVICE response format]
   </device_props>
   <device_props id=”IdN”>
    [see the GET_DEVICE response format]
   </device_props>
</device_list>
```


