## LOCK\_STATUS\_CHANGED

Sent in when a lock status changes for any reason.


### Name

`LOCK_STAUS_CHANGED ()`


| Parameter               | Type | Description                                                      |
| ----------------------- | ---- | :--------------------------------------------------------------- |
| LOCK STATUS             | STR  | Required parameter: unknown, locked, unlocked, or fault.         |
| LAST ACTION DESCRIPTION | STR  | Optional parameter.                                              |
| SOURCE                  | STR  | Optional parameter: the source that affected the status change.  |
| MANUAL                  | BOOL | Optional parameter: true, false, assumed false if not specified. |


### Returns

`None`
 