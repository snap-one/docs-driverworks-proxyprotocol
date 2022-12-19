# Light V2 Events

The following are System Events that are provided and managed by the Proxy.  These can be used for Composer Programming or other drivers to monitor the changes of a values reflected in a LightV2 proxy.



`Light On`
Light has turned On. Event ID = 5100.


`Light Off`
Light has turned Off. Event ID = 5101.


`Light Brightness Changed`
The brightness of the light has changed. Event ID = 4001.


`Light Brightness Changing`
The brightness of the light is changing. Event ID = 4000.


`Light Color Changed`
The color of the light has changed. Event ID = 4003


`Light Color Changing`
The color of the light is changing. Event ID = 4002

`Old Light Level Changed`
The light level of the light has changed and is at the final brightness. Event ID = 5000.



















**Keypad Events**

An event is fired when something happens to one of the buttons on the device. The pattern for determining the Event ID is: 

5001 + action + (btnID \* 5). 

The actions are:

- Release = 0
- Push = 1
- Single Click = 2
- Double Click = 3
- Triple Click = 4

The button IDs are determined by the protocol driver, but the standard ordering is:

- Top = 0
- Bottom = 1
- Toggle = 2