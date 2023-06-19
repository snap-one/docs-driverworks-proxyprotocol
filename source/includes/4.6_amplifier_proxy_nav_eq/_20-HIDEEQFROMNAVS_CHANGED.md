## HIDE\_EQ\_FROM\_NAVS \_CHANGED

Navigator EQ notification that the equalizer should be shown or hidden from Navigator. This must be sent with a value of False to enable the EQ functionality in Navigator.


### Signature

`HIDEEQFROMNAVS_CHANGED`


| Parameter | Description |
| --- | --- |
| int | OUTPUT: OutputBindingID |
| bool | ENABLED: True to hide this output from Navigators. False to allow output eq controls to be shown.  Default is True. |


### Returns

`None`


### Example

```lua
-- Notify Hide (or show) Navigator EQ for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "HIDEEQFROMNAVS_CHANGED", { OUTPUT = "4002", ENABLED = false }, "NOTIFY")
```
