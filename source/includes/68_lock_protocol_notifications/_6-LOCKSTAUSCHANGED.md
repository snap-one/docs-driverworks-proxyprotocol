## LOCK STATUS  CHANGED

Sent in when a lock status changes for any reason.


### Signature

`LOCK_STAUS_CHANGED ()`


| Parameter | Description |
| --- | --- |
| str |LOCK STATUS: Required parameter: unknown, locked, unlocked, or fault. |
| str |LAST ACTION DESCRIPTION: Optional parameter. |
| str |SOURCE: Optional parameter: the source that affected the status change. |
| bool |MANUAL: Optional parameter: true|false, assumed false if not specified. |


### Returns

`None`
