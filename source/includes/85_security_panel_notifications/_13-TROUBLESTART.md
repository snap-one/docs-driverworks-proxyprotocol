## TROUBLE\_START

List trouble that the panel is having on the Composer Property Page and on each of the Navigator partition screens.  


| Parameter    | Type | Description                                                                       |
| ------------ | ---- | :-------------------------------------------------------------------------------- |
| TROUBLE TEXT | STR  | Text listing the type of trouble. “For example: “Battery", "Communication", etc.) |
| DENTIFIER    | NUM  | Unique number for this instance of trouble.                                       |


### Example

```lua
C4:SendToProxy(TargetBindingID, "TROUBLE_START", { TROUBLE_TEXT = "Battery", IDENTIFIER = 10 }, "NOTIFY")
```

