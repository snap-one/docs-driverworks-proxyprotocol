## SET AEC ENABLE 

This command is issued to enable or disable automatic echo cancellation on intercom devices that support this capability.


### Signature

`C4: SET_AEC_ENABLE  ()`


| Parameter | Description |
| --- | --- |
| int | A Boolean flag indicating whether enable or disable auto-echo cancellation.  Enabled = 1, true, yes or on.  Disabled = 0, false, no or off. |


### Returns

`None`


### Example

```
<SET_AEC_ENABLED>
    <aecEnabled>[0]</aecEnabled>
</SET_AEC_ENABLED>
```
