## EDIT\_GROUP

This command is issued to rename the specified intercom call group. Note that the name of the “All” group cannot be changed

### Signature

`EDIT_GROUP ()`


| Parameter | Description |
| --- | --- |
| str | The name of the call group to which the specified endpoint should be added. |
| str | newName: The new name for the specified call group. |


### Returns

`None`


### Example

```lua
<EDIT_GROUP>
  <name>[mydevice]</name>
  <newName>[mynewdevice]</newName>
</EDIT_GROUP>
```

