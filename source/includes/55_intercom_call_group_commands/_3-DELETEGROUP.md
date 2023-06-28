## DELETE\_GROUP

This command is issued to delete an intercom call group. Note that the “All” group cannot be deleted. 

### Signature

`DELETE_GROUP ()`


| Parameter | Description |
| --- | --- |
| str | The name of the call group to which the specified endpoint should be added. |



### Returns

`None`


### Example

```lua
<DELETE_GROUP>
  <name>[mydevice]</name>
</DELETE_GROUP>
```

