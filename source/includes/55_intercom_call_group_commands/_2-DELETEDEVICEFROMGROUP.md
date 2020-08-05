## DELETE DEVICE FROM GROUP

This command is issued to remove the specified intercom endpoint from the specified call group. Attempting to delete a device from the “All” group will result in a command failure.

### Signature

`DELETE_DEVICE_FROM_GROUP ()`


| Parameter | Description |
| --- | --- |
| str | The name of the call group to which the specified endpoint should be added. |
| num | The proxy id of the intercom endpoint that should be added to the call group. |


### Returns

`None`


### Example

```lua
<DELETE_DEVICE_FROM_GROUP>
  <name>[mydevice]</name>
  <idDevice>[10]</idDevice>
</DELETE_DEVICE_FROM_GROUP>
```
