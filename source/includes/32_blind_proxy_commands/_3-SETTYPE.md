## SET\_TYPE

Sets the blind type for the proxy.


### Name

`SET_TYPE ()`


| Parameter | Type | Description                     |
| --------- | ---- | ------------------------------- |
| SET\_Type | NUM  | Enumeration of the blind  type. |

Blind Types:

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

If set to -1 then a dealer can select a choice from a pulldown in the proxy property control. This Notification sends DataToUI of blind setup xml.


### Returns

`None`

