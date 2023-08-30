## CALL\_RESUMED

**NOTE:** The CALL\_RESUMED notify is currently deprecated and not available for use.\_


This notification is issued when a session is resumed, it is sent to the initiator and all receiver(s) involved in the specified session.


### Signature

`CALL_ RESUMED ()`


| Parameter | Description |
| --- | --- |
| num | The Device ID of the Proxy. |
| num | The Session ID of the SIP session.  Session ID is established when a call is initiated and serves as a unique identifier of the call. |

