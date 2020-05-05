## DELETE GROUP

This command is issued to delete an intercom call group. Note that the “All” group cannot be deleted. 

### Signature

`C4:DELETE_GROUP ()`


| Parameter | Description |
| --- | --- |
| str | The name of the call group to which the specified endpoint should be added. |



### Returns

`None`


### Example

```
<DELETE_GROUP>
  <name>[mydevice]</name>
</DELETE_GROUP>
```

