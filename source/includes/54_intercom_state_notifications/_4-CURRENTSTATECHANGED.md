## CURRENT\_STATE\_CHANGED

This notification is issued by the protocol  when the endpoint’s current state has changed.


### Signature

`CURRENT_STATE__CHANGED ()`


| Parameter | Description                                                                                                         |
| --------- | ------------------------------------------------------------------------------------------------------------------- |
| num       | currentState - Numeric value indicating the current state of the device. (0=not ready, 1=idle, 2=busy, 3=max calls) |


### Example

```lua
<device_state proxyid =[10]>
   <currentState>[2]</currentState>
</device_state>
```
