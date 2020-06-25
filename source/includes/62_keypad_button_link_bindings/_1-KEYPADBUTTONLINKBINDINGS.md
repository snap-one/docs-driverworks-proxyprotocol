## KEYPAD BUTTON LINK BINDINGS

BUTTON_LINK bindings are a way for drivers to interact with other drivers that either expose a physical or virtual Keypad Button or for drivers that want to integrate with drivers that have a physical or virtual button.  Button State and LED State information are the information that can be passed between the drivers.  For example, a Control4 Keypad exposes a BUTTON_LINK binding that the Tune-In driver integrates with so a user can select a playlist or change songs via a Control4 Physical Keypad.  

BUTTON_LINK was designed and assumes button and led functionality is the same between all keypad button hardware existing in the Control4 project, which causes some drivers to have to sometimes have incomplete or even fake functionality, ie: Button Release or Button Color functionality because some Non-Control4 physical keypads do not have LEDs.  Also hardware/drivers do not have an API that allows drivers to interrogate hardware for what is supported.  Some new devices also have specific double and triple click support which is newer. Note that older drivers were not updated to support those multi-press calls that go over BUTTON_LINK bindings.  There is also no limit to what can be sent over a BUTTON_LINK as it's purely just a passage. 


A driver making use of another drivers physical keypad buttons will typically support the following Commands and Notifies and will check the binding ID of the messages of the bound call command to know which button (BUTTON_LINK) the message applies to.

**Commands**

`DO_PUSH`
Button was Pushed. Driver can expect to get a CLICK or RELEASE sometime in the future.  If a driver does not care if the button is held or clicked, Control4 recommends executing native driver's functionality on Press rather than waiting for the upcoming CLICK or RELEASE.

`DO_CLICK`
Button was Clicked, not held. Driver can expect to get a CLICK or RELEASE sometime in the future.  If a driver does not care if the button is held or clicked, Control4 recommends executing native driver's functionality on Press rather than waiting for the upcoming CLICK or RELEASE

`DO_RELEASE`
Button was finally released. Note that drivers might tie up Director between a users physical PUSH and RELEASE. For example, a half second push may appear to the driver as many seconds of being held. This could result in causing unwanted results such as "runaway" volume or light ramping. There is no way to detect or work around this at the current time.


`REQUEST_BUTTON_COLORS`
Causes the driver to respond back with `BUTTON_COLORS` and `MATCH_LED_STATE` calls to let the other end of the binding know what the colors and state of them are.\_ 

`SET_BUTTON_COLOR`
Used to set the color of a button, this command name can be unique or non-existent for some drivers but this should be followed to make mass setting LED's possible from driver to driver.

| Parameter | Description |
| --- | --- |
| str | BUTTON ID: String of the button, often used by a driver or proxy to lookup which of its buttons its setting. Sometimes it can be auto determined by which binding it came in on. |


**Notifications**

`BUTTON_COLORS`

| Parameter | Description |
| --- | --- |
| str |ON COLOR: COLOR STR type, value of string such as "ffccbb"
| str |OFF COLOR: COLOR STR type, value of a string such as "000000"


`MATCH_LED_STATE`

| Parameter | Description |
| --- | --- |
| bool |STATE: Boolean if the Off (0/false) or On (1/true) color should be active. |


