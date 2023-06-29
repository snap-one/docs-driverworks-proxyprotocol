## STATE\_CLOSED

Relay remains in the closed state. Does not indicate a change in state.


### Signature

`STATE_CLOSED ()`


### Parameters

`None`


### Returns

`None`


### Usage Note

Send `STATE_CLOSED` when the device initializes rather than `CLOSED`. The driver will ignore the `STATE_CLOSED` from the standpoint of events since it is not a state change but just a notification of the current state.
