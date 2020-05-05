## STATE OPENED

Relay remains in the open state. Does not indicate a change in state.


### Signature

`C4:STATE_OPENED ()` 


### Parameters

`None`


### Returns

`None`


### Usage Note

Send `STATE_OPENED` when the device initializes rather than `OPENED`. The driver will ignore the `STATE_OPENED` from the standpoint of events since it is not a state change but just a notification of the current state.

