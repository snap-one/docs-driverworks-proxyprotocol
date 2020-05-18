## AUTO ANSWER CHANGED

This notification is issued when a call is accepted, it is sent to the initiator and the receiver involved in accepting the specified session.


### Signature

`C4:AUTO_ANSWER_CHANGED ()`


| Parameter | Description |
| --- | --- |
| int | The proxy device id of the intercom endpoint whose device state information is being returned |
| int | autoAnswer: Boolean flag indicating the current state for this setting. (0=false, 1=true) |


### Example

```lua
<device_state id=[10]>
   <autoAnswer>[1]</autoAnswer>
</device_state>
```
