## ARM FAILED

An attempt to arm the partition failed.  The two most common reasons are because a user code is required to arm this partition or because one or more unbypassed zones are open.


### Signature

`ARM_FAILED ()`


| Parameter | Description |
| --- | --- |
| str | ACTION: Supported values include: “keypad”: Will cause Navigator to ask for a user code and then retry.  
| | “bypass”: Will cause Navigator to show a list of zones that are in fault and ask the user if they wish to continue. If continue chosen, the arm command will be resent.  However, it will try to bypass each faulted zone before it tries to arm again. |
| | “NA”: Failed for some other reason.  Navigator will take no further action on the arming. |
| | | str | NTERFACE\_ID: Commands receiveD from Director will have an interface\_id string sent as one of the parameters.  This is a unique string that identifies where the command originated. When a response such as a failure is sent, it should only display on the UI that originated the command.  To support this, the INTERFACE\_ID string is sent back with the notification. Only the original UI will show the results of this notification. |



### Returns

`None`


### Example

```lua
C4:SendToProxy(TargetBindingID, "ARM_FAILED", { ACTION = tostring(bypass) }, "NOTIFY")
```
