## GET GROUP LIST

This request is issued to obtain the group list of all of intercom call groups in the project except for the “All” group. 


### Signature

`C4:GET_CUSTOM_BUTTONS ()`


| Request Parameter | Description |
| --- | --- |
| num | The group ID of the call group. |
| str | The name of the call group.


### Example

```lua
<groups>
  <group>
   <id>[3]</id>
   <name>[group one]</name>
  </group>
  <group>
    <id>[4]</id>
    <name>[group two]</name>
  </group>
</groups>
```

