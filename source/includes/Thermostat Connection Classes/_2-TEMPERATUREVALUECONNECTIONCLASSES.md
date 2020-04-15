## TEMPERATURE VALUE CONNECTION CLASSES

**Commands**

## VALUE INITIALIZED
The value has been initialized. OnBindingChanged will cause this command to be sent automatically when the sending device goes Online.

### Signature

`C4:VALUE_INITIALIZED ()`

| Parameter | Description |
| --- | --- |
|str | STATUS : Default is the status after first loading a driver and the value has never been set. `active` - Status if the value is active. `last_known `- The Last value received. The device either went offline or it has not been heard from since a reboot.
| int | TIMESTAMP: Timestamp of when the last value was received. |



## VALUE CHANGED 
The value has changed.

### Signature

`C4:VALUE_CHANGED ()`

| Parameter | Description |
| --- | --- |
| int | CELCIUS - Float - Celsius temperature value. |
| int | FAHRENHEIT - Float - Fahrenheit temperature value.  |
| int | TIMESTAMP - Timestamp When the change occurred. |



## VALUE UNAVAILABLE
The value is possibly no longer accurate. OnBindingChanged, device went Offline, etc

### Signature

`C4:VALUE_CHANGED ()`

| Parameter | Description |
| --- | --- |
| str | STATUS: offline - Device went offline or was unbound |

