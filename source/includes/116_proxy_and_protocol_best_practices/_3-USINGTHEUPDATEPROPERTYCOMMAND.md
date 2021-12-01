## USING THE UPDATE PROPERTY COMMAND

The `UPDATE_PROPERTY` command is a non proxy-specific function that can be called from any device to change a property of any other device. This command modifies a Property of a device that is currently in a Control4 project. The command is sent from a driver other than that of the device who's property is being modified. This supports that ability to modify device properties externally. 

Consider the following scenarios where `UPDATE_PROPERTY` may be useful:

- A Primary device that is aware of the configuration of Secondary devices. The Primary device can use `UPDATE_PROPERTY` to send new configuration data to Secondary devices and ultimately to set the properties of the Secondary devices.
- The replacement of an obsolete device driver with a new driver. Instead of manually copying a device’s properties to a new driver’s properties, a dealer could use the `UPDATE_PROPERTY` to automate this process.


| Parameter | Description |
| --- | --- |
| str | Name: Name of the Property that is being modified. |
| int | Value: The new value of the Property that is being modified. |


### Returns

`None`


### Example

`C4:SendToDevice(deviceId, "UPDATE_PROPERTY", {Name = propName, Value = newPropValue})`
