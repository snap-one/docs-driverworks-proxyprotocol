## CLEAR\_ZONE\_LIST

Removes all the zones from a partition's list.  Usually precedes new messages that will build that list back up.


### Signature

`CLEAR_ZONE_LIST ()`


### Parameters

`None`


### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "CLEAR_ZONE_LIST" "NOTIFY")
```
