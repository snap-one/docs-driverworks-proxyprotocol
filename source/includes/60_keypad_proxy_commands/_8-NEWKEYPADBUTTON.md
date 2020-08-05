## NEW KEYPAD BUTTON

Used to create a new button on the keypad. This is sent to the protocol by the proxy when the proxy is loaded. Thus the protocol doesn't have to store all its buttons settings, the proxy will do it.


### Signature

`NEW_KEYPAD_BUTTON ()`


| Parameter | Description |
| --- | --- |
| BUTTON ID | The ID of the button being changed |
| NAME | The name of the button (optional) |
| ON COLOR (string) |  The on/press color for the button (optional) |
| OFF COLOR  (string) |The off/release color for the button (optional) |
| BUTTON BEHAVIOR (INT) | The behavior for the button (optional) |
| LED BEHAVIOR (INT) | The LED behavior for the button (optional) |
| SLOTS | The number of slots the button takes up on the keypad. |

### Returns

`None`

