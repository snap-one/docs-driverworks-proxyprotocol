## DISARM\_FAILED

Notification sent when an attempt to disarm the panel failed. This is typically due to an invalid user code.


| Parameter | Description |
| --- | --- |
| str | NTERFACE\_ID: Commands receiveD from Director will have an interface\_id string sent as one of the parameters.  This is a unique string that identifies where the command originated. When a response such as a failure is sent, it should only display on the UI that originated the command.  To support this, the INTERFACE\_ID string is sent back with the notification. Only the original UI will show the results of this notification. |


### Example

```lua
C4:SendToProxy(TargetBindingID, "DISARM_FAILED", { INTERFACE_ID = ID }, "NOTIFY")
```
