## Proxy Interface

The Proxy Interface is used to update the Variables defined in the next section.

A driver can update the currently enabled buttons and transports by making SendToProxy calls. SendToProxy does not necessarily need to be called unless the driver wants to change the buttons. If no changes from the provided default values in the Variables are needed; the Capability XML can simply be added to the driver and no other calls need to be made.

The SendToProxy call supports the use of the following parameters:

| Parameter | Description |
| --- | --- |
| replace | Replaces the entire list with the given list which is a comma separated list of button IDs. |
| add | Add a single button. A position is required for this parameter. |
| remove | Remove a single button. |

### Example
To update the large dashboard to show just buttons with the IDs of PLAY and PAUSE:

`C4:SendToProxy(PROXY_BINDING, "UPDATE_TRANSPORTS_DASHBOARD_LARGE", {replace = "PLAY,PAUSE"})`


### Example
To update the small dashboard: 

`C4:SendToProxy(PROXY_BINDING, "UPDATE_TRANSPORTS_DASHBOARD_SMALL", {replace = "PLAY,PAUSE"})`


### Example
To update supported transport controls: 

`C4:SendToProxy(PROXY_BINDING, "UPDATE_TRANSPORTS_SUPPORTED", {replace = "PLAY,PAUSE"})`


### Example
To update button bar buttons: 

`C4:SendToProxy(PROXY_BINDING, "UPDATE_TRANSPORTS_BUTTONS", {replace = "PLAY,PAUSE"})`


### Example
To use the add parameter, a position must also be specified to add the button. This is a zero-based index. For example, to add PLAY at index 5:

`C4:SendToProxy(PROXY_BINDING, "UPDATE_TRANSPORTS_DASHBOARD_LARGE", {add = "PLAY", position = 5})`


### Example
To remove the button with the ID of PLAY from the large dashboard:

`C4:SendToProxy(PROXY_BINDING, "UPDATE_TRANSPORTS_DASHBOARD_LARGE", {remove = "PLAY"})`
