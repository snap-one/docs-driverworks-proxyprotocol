## ICON CHANGED

Command sent to the proxy when the icon state has changed.


### Signature

`C4:ICON_CHANGED ()` 


| Parameter | Description |
| --- | --- |
| str | icon:  value which references an icon state name defined in the [`display_icons`]() capability or an empty string to set the default icon. |
| str |icon description: Value of a human readable string describing the icon state. This is used in the List Navigator in place of the icon. |


### Returns

`None`


### Example

`C4:SendToProxy(5001, "ICON_CHANGED", {icon="Settings-on", icon_description="Settings are on"})`

