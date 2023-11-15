# Intercom Proxy Terminology 

The following terms are specific to the Control4 Intercom Proxy and their use in developing a door station or door station like driver. Note that this content does not include the scope of developing a touch panel to support intercom use.


**Intercom Call Commands** –  Include a set of commands that are sent from the Intercom Proxy to the door station device that is supported by your driver. An example of an Intercom Proxy Command is START\_CALL. When your driver receives the START\_CALL command, it must handle the command in a manner that enables your device to begin a call.


**Intercom Call Notifications** -  Consist of “notifies” that are sent from the device you are supporting, via your driver, to the Intercom Proxy. For example, when your driver receives a START\_CALL command, it will send a CALL_\STARTED notification to the Intercom Proxy.


**Intercom Call Requests** - These functions represent requests that are sent from your device driver to the Intercom Proxy for various sets of Call data. For example, when needed, your driver may send the Intercom Call Request of GET\_DEVICE\_LIST. The GET\_DEVICE\_LIST request is a function for gathering information about other devices on the network that  might communicate with your device. Information returned includes data such as whether another device has a camera, does it include a display, etc.


**Intercom State Commands** - These functions consist of commands that impact the state of the device you are writing a driver for. For example, your driver may receive a State Command of SET\_RINGER\_VOLUME from the Intercom Proxy. SET\_RINGER\_VOLUME will be sent with a numerical value indicating the new ringer volume level. Your driver will need to receive this state command and adjust the ringer volume on your device accordingly.


**Intercom State Notifications** - These functions consist of “notifies” that are sent from the device you are supporting, via your driver, to the Intercom Proxy. For example, when your driver receives the State Command of SET\_RINGER\_VOLUME, it needs to send a State Notification of RINGER\_VOLUME\_CHANGED that includes the new ringer volume value.


**Intercom State Requests** - These functions  represent requests that are sent from your device driver to the Intercom Proxy for various sets of device state data. For example, when needed, your driver may send the Intercom Call Request of GET\_STATE\_LIST. This request returns the device states for all of the intercom endpoints in the project.


**Intercom Call Group Requests** - Currently, this consists of one function: GET\_GROUP\_LIST which can be used by your driver to obtain the group list of all of intercom call groups in the project.


**Intercom Capabilities** -  These  functions  consist of Boolean XML elements that need to be defined in your driver. They represent functionality supported by your device such as do not disturb support, camera inclusion or its ability to play a door chime.


**Intercom Events** - Events are useful to define in your driver as they provide an opportunity for ComposerPro programming to occur based on them being fired. For example, if the speaker_volume_changed Event is defined in your driver and that Event fires when the speaker volume of your device changes, it would be possible (through programming in ComposerPro) to modify the speaker volume of other intercom devices in the project.


**Intercom Conditionals** - Conditionals are useful to define in your driver as they also provide an opportunity for ComposerPro programming to occur based on their state. For example, if the In a Call conditional is set to true, the device that reported this conditional could be displayed as busy on Navigators. 


**Intercom Variables** – The Intercom Proxy supports three Variables which can also be used in ComposerPro programming when defined in your driver. For example, the CALL\_DURATION Variable can be assigned a time limit for a call, If that limit is exceeded, the call can be terminated.
