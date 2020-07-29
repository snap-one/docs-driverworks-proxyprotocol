## TROUBLE START

List trouble that the panel is having on the Composer Property Page and on each of the Navigator partition screens.  


| Parameter | Description |
| --- | --- |
| str | TROUBLE\_TEXT: Text listing the type of trouble. “For example: “Battery", "Communication", etc.)  |
| num | IDENTIFIER:  Unique number for this instance of trouble. | \_ 


### Example

```lua
C4:SendToProxy(TargetBindingID, "TROUBLE_START", { TROUBLE_TEXT = "Battery", IDENTIFIER = 10 }, "NOTIFY")
```

