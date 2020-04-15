## HUMIDITY VALUE CONNECTION CLASSES

**Commands**

## VALUE INITIALIZED
The value has been initialized. OnBindingChanged will cause this command to be sent automatically when the sending device goes Online.

### Signature

`C4:VALUE_INITIALIZED ()`


| Parameter | Description |
| --- | --- |
| str | STATUS: Default is the status after first loading a driver and the value has never been set. `active` - Status if the value is active. `last_known` - The Last value received. The device either went offline or it has not been heard from since a reboot. |
| int | TIMESTAMP:  Timestamp of when the change occurred. |




## VALUE CHANGED
The value has changed.

### Signature

`C4:VALUE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| int | VALUE |
| int | TIMESTAMP:  Timestamp of when the change occurred. |




## VALUE UNAVAILABLE
The value is possibly no longer accurate. OnBindingChanged, device went Offline, etc

### Signature

`C4:VALUE_UNAVAILABLE ()`


| Parameter | Description |
| --- | --- |
| str | STATUS: offline - Device went offline or was unbound. |