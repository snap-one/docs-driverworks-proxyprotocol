## CODE\_REQUIRED

Sets a flag that Navigator will use when an arm command is attempted.  If the flag is true, Navigator will ask for a user code before it sends the arm command.


| Parameter | Description |
| --- | --- |
| bool | CODE\_REQUIRED\_TO\_ARM: “true" if the user code should be sent with the arm command. |


### Example


```lua
C4:SendToProxy(TargetBindingID, "CODE_REQUIRED", { CODE_REQUIRED_TO_ARM = true }, "NOTIFY")
```
