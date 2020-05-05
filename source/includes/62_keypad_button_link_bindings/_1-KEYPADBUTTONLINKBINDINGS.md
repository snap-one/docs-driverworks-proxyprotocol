## KEYPAD BUTTON LINK BINDINGS

**Commands**

`DO_PUSH`
﻿Button was Pushed. Driver can expect to get a CLICK or RELEASE sometime in the future.  If a driver does not care if the button is held or clicked, Control4 recommends executing native driver's functionality on Press rather than waiting for the upcoming CLICK or RELEASE.

`DO_CLICK`
Button was Clicked, not held. Driver can expect to get a CLICK or RELEASE sometime in the future.  If a driver does not care if the button is held or clicked, Control4 recommends executing native driver's functionality on Press rather than waiting for the upcoming CLICK or RELEASE

`DO_RELEASE`
﻿Button was finally released. Note that drivers might tie up Director between a users physical PUSH and RELEASE. For example, a half second push may appear to the driver as many seconds of being held. This could result in causing unwanted results such as "runaway" volume or light ramping. There is no way to detect or work around this at the current time.


`REQUEST_BUTTON_COLORS`
Causes the driver to respond back with `BUTTON_COLORS` and `MATCH_LED_STATE` calls to let the other end of the binding know what the colors and state of them are._ 

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


