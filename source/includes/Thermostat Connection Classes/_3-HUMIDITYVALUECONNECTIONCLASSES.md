## HUMIDITY VALUE CONNECTION CLASSES

**Commands**

## VALUE INITIALIZED
The value has been initialized. OnBindingChanged will cause this command to be sent automatically when the sending device goes Online.

### Signature

`C4:VALUE_INITIALIZED ()`

| Parameter | Description |
| --- | --- |
STATUS (str)
default is the status after first loading a driver and the value has never been set.
active - Status if the value is active
last_known - The Last value received. The device either went offline or it has not been heard from since a reboot.
TIMESTAMP - Timestamp of when the change occurred.




## VALUE CHANGED
The value has changed.

### Signature

`C4:VALUE_INITIALIZED ()`

| Parameter | Description |
| --- | --- |
VALUE - Integer
TIMESTAMP - Timestamp of when the change occurred.




## VALUE UNAVAILABLE_ ### Signature

`C4:VALUE_INITIALIZED ()`

| Parameter | Description |
| --- | --- |

The value is possibly no longer accurate. OnBindingChanged, device went Offline, etc
Parameters
STATUS - (str) offline - Device went offline or was unbound