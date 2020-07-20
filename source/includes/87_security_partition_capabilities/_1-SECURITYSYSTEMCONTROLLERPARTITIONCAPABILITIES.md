
The following Capabilities are supported with the Security System Controller Partition:

`ui_version` 
Integer. Defaults to 1.
If the value is 1 then the original security user interface is used and and the assumption is that the protocol driver would only know how to handle the `BUTTON_PRESS` command.  A value of 2 means that the new user interface is used.  If the interface changes in the future, this number may increase again. Note that the `BUTTON_PRESS` command is being deprecated.

`arm_states`
String. Default to “Home, Away”
A comma delimited string containing the possible arm states this system supports.

`has_fire`
Boolean. Defaults to false.
True if this partition supports the “Fire” emergency button.

`has_medical`
Boolean. Defaults to false.
True if this partition supports the “Medical” emergency button.

`has_police`
Boolean. Defaults to false.
True if this partition supports the “Police” emergency button.

`has_panic`
Boolean. Defaults to false.
True if this partition supports the “Panic” emergency button.

`functions`
String. Default to ""
A comma delimited string containing the functions supported by the protocol driver.

`star_label`
string Default to `*`
The text that will be shown on the  `* button` on the keypad.

`pound_label`
string Default to “#”
The text that will be shown on the # button on the keypad.
 
`button_A` 
xml string
\<visible\>true\</visible\>
Designates whether button “A” will be visible on the UI keypad.
`<label>This is Button A</label>`
The text that will appear on button “A” on the UI keypad (if visible)  Defaults to “A”
 
`button_B`
xml string
\<visible\>true\</visible\>
Designates whether button “B” will be visible on the UI keypad.
`<label>This is Button B</label>`
The text that will appear on button “B” on the UI keypad (if visible)
Defaults to “B”
 
`button_C`
xml string
`<visible>true</visible>`
Designates whether button “C” will be visible on the UI keypad.
`<label>This is Button C</label>`
The text that will appear on button “C” on the UI keypad (if visible)
Defaults to “C”
 
`button_D`
xml string
`<visible>true</visible>`
Designates whether button “D” will be visible on the UI keypad.
`<label>This is Button D</label>`
The text that will appear on button “D” on the UI keypad (if visible)
Defaults to “D”

`supports_virtual_keypad`
Boolean Defaults to true.
True if the panel supports raw key presses being passed by the software directly to the hardware; usually used for panel programming or setup.