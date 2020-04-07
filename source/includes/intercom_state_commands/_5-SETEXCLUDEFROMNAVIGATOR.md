## SET EXCLUDE FROM NAVIGATOR 

This command is issued to toggle the visibility of the intercom endpoint in a proxy user interface. This command will result in an `EXCLUDE_FROM_NAVIGATOR_CHANGED` notification to the proxy.


### Signature

`C4: SET_EXCLUDE_FROM_NAVIGATOR ()`


| Parameter | Description |
| --- | --- |
| bool | Boolean flag indicating the new state for this setting. (0=false, 1=true) |


### Returns

`None`


### Example

```
<SET_EXCLUDE_FROM_NAV>
   <excludeFromNav>[1]</excludeFromNav>
</SET_EXCLUDE_FROM_NAV>
```
