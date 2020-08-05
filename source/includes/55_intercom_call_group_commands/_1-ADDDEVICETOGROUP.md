## ADD DEVICE TO GROUP

This command is issued to add the specified intercom endpoint to the specified call group. 

### Signature

`ADD_DEVICE_TO_GROUP ()`


| Parameter | Description |
| --- | --- |
| str | The name of the call group to which the specified endpoint should be added. |
| num | The proxy id of the intercom endpoint that should be added to the call group. |


### Returns

`None`


### Example

```lua
ADD_DEVICE_TO_GROUP>
  <name>[mydevice]</name>
  <idDevice>[10]</idDevice>
</ADD_DEVICE_TO_GROUP>
```


