## CREATE GROUP

This command is issued to create  a new intercom call group. Note that the text “All” is a reserved group name. The command will fail if this call is made with the group name “All”. 

### Signature

`C4:CREATE_GROUP ()`


| Parameter | Description |
| --- | --- |
| str | The name of the call group to which the specified endpoint should be added. |



### Returns

`None`


### Example

```
<CREATE_GROUP>
  <name>[mydevice]</name>
</CREATE_GROUP>
```

