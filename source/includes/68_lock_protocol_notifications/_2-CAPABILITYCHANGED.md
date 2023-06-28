## CAPABILITY\_CHANGED

Sent when a capability changes; or when requested by the protocol driver command `REQUEST_CAPABILITES`, and a capability has changed from what is defined in the driver capabilities XML


### Signature

`CCAPABILITY_CHANGED ()`


| Parameter | Description |
| --- | --- |
| str |NAME: Required parameter: The name of the setting is its XML tag as defined in `<lock_setup>`.
| str |VALUE: Required parameter: The capabilities new value.
