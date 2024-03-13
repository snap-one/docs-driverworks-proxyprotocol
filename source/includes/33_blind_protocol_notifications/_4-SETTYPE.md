## SET\_TYPE

Configuration Notification used by the protocol to inform the proxy that the driver is a particular blind type.  If this is used, the proxy will disable the pulldown from being selectable by a dealer.

### Name

`SET_TYPE ()`


| Parameter | Type | Description                    |
| --------- | ---- | ------------------------------ |
| SET  TYPE | INT  | Enumeration of the blind type. |

Movement Types:

- 0 - Shade (Default as all coverings are considered to be Shades in the industry)
- 1 - Group
- 2 - Blind (Since a blind has slates/louvers that often move, a blind can be bound to a louver movement for association)
- 3 - Louver
- 4 - Curtain
- 5 - Shutter
- 6 - Blackout
- 7 - Opaque Glass
- 8 - Awning
- 9 - Door
- 10 - Screen

If set to -1 then a dealer can select a choice from a pulldown in the proxy property control.


### Returns

`None`


### Usage Note

 This Notification sends DataToUI of: `blind_setup xml`.