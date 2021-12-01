## ICON CHANGED

Notification sent to the proxy to change the driver's icon.


### Signature

`ICON_CHANGED` 


| Parameter | Description |
| --- | --- |
| icon | str:  value which references an icon state name defined in the [`display_icons`]() capability or an empty string to set the default icon. |
| icon\_description | str: Value of a human readable string describing the icon state. This is used in the List Navigator in place of the icon. |


### Returns

`None`


### DataToUI

Sends “icon” DataToUI: `<icon>Settings-on</icon>`

Also sends “icon\_description” DataToUI: `<icon_description>Settings are on</icon_description>`


### Example

`C4:SendToProxy(5001, "ICON_CHANGED", {icon="Settings-on", icon_description="Settings are on"})`



