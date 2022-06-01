# Light V2 Extras Interface Library

### Overview
Extras are a way for driver developers to expose unique hardware functionality that users can interact with on a UI/Navigator.  This functionality bypasses the need for a proxy to know about the unique features and how to handle them.  A protocol driver notify is used to pass the Extras XML information from the protocol driver to the proxy, where the proxy caches the xml strings for current setup and state information. The UI  uses a UI\_REQUEST as needed to get the information if the UI has just rebooted/started/loaded and then the UI will get updates of these xml strings if it is listening for dataToUI's from the device.  Extras objects are accessible through the "Extras Tab" located on the main Navigator screen for the Proxy.


### Capabilities
The has\_extras capability must be set to true to support the use of Extras. The library will automatically (via dynamic capability) set the has\_extras capability when a first Section is created. Also, when the last section is removed, the has\_extras capability will be disabled. The Extras class does not implement class destructor as it is not supported in Lua 5.1 and Lua JIT. In the case of setting the Extras class instance to nil, the Extras:cleanCapability() method should be called previously.

### Protocol Notify and Proxy Messages
There are two notifies a driver must make to the proxy where this information is forwarded immediately to any UI's listening for dataToUI on the proxy and the information is also cached for future UI's to request: EXTRAS\_SETUP\_CHANGED and EXTRAS\_STATE\_CHANGED.  

Whenever a driver changes values that are reflected in either the setup or state xml, it must make the notify to the proxy with the updated information.  This includes if hardware or a feature is added or removed, a value for one of the objects was updated, and so on.  

It is also advisable for protocol drivers to send this data either on initialization of the driver if the values are not likely to change when hardware comes online, or perhaps when the hardware comes online and the extras commands will be able to succeed.  

In addition, it could be advisable that the state of objects is changed to hidden when hardware and/or disabled features are not available rather than sending new extras\_setup notifies as this may cause a UI to redraw the extras page and reset defaults while a user is interacting with the Extras page on a UI.


### EXTRAS SETUP CHANGED

Update the Extras Setup, displayed in the UI 


### Signature

`EXTRAS_SETUP_CHANGED ()`


| Parameter | Description |
| --- | --- |
| XML | XML text string of XML matching the Preset Schedule schema. Comes through to the UI as `extras_setup`. Note that as of OS 3, sending only a singular XML string is supported. For example, sending an array of Extras can result in Navigator performance issues. |


### Returns

`None`


### EXTRAS STATE CHANGED

Update the Extras Setup, displayed in the UI 


### Signature

`EXTRAS_STATE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| XML | XML text string of XML matching the Preset Schedule schema. To UI comes through as `extras_state`. |


### Returns

`None`



### How UI's handle Extras objects

UI's will display objects in the order they are read in the EXTRAS\_SETUP xml.  If an object needs to have a default selection, number or string, the UI looks at the value attribute for the default.  If no value is specified in the EXTRAS\_SETUP the UI will default to a behavior listed below for each object type.

When a user changes a value on a UI, the UI will immediately send the command associated with that object down to a protocol driver as a command.  The UI waits for a response that the protocol driver has handled the command and the protocol driver must send an updated EXTRAS\_STATE notify for the object.  

The EXTRAS\_STATE does not need to include all states of all objects, only the states of the objects it wants to update (or acknowledged) it has received but it could contain more than just one objects updated state.  A driver could also respond back with just the `<extras_state><extra><object id="1"></extra></extras_state>` if it wanted to acknowledge the command succeeded but not update the value.  If a UI that sent the command does not get a response in 10 seconds, it will change the value of the object back to what it was prior to what the user had changed it from.
