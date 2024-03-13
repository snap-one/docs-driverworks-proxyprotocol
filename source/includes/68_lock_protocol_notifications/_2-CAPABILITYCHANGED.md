## CAPABILITY\_CHANGED

Sent when a capability changes; or when requested by the protocol driver command `REQUEST_CAPABILITES`, and a capability has changed from what is defined in the driver capabilities XML


### Name

`CAPABILITY_CHANGED ()`


| Parameter | Type | Description                                                                              |
| --------- | ---- | ---------------------------------------------------------------------------------------- |
| NAME      | STR  | Required parameter: The name of the setting is its XML tag as defined in `<lock_setup>`. |
| VALUE     | STR  | Required parameter: The capabilities new value.                                          |
