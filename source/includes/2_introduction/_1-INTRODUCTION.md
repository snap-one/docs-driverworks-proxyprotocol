
## Proxies (Commands)

A proxy driver is an interface to the Control4 system for a set of devices that share common functionality. For instance, most DVD disc changers have common controls such as PLAY, STOP, PAUSE and FAST FORWARD.  The disc changer proxy allows for a common user interface to control all disc changers.  The Control4 system (Director) sends information to and receives information from the proxy drivers.  The proxy drivers send information to and receives information from the protocol drivers.
Remember, your DriverWorks driver interacts with the proxy driver which then interacts with the system.  As a driver developer you will be relying on this proxy to provide status (notification) to the Control4 system for the device you are controlling.  You will also receive commands from the system that you will act on to control the device.  These commands and notifications are at the heart of what you will be implementing in your driver.  Essentially your driver is becoming the go-between from the Control4 system and your device with the proxy driver giving structure to the commands and notifications which you will be implementing.
Your driver can facilitate communications with multiple types of proxies for a single device. As an example, a Security System driver will utilize both the Security proxy and the Contacts proxy. These additional proxies are configured in the \<connections\> section of the .c4z.


## Protocol (Notifications)

Two similar devices may have the same functionality but utilize a very different command set.  A protocol driver provides the device-specific information needed to communicate with the Control4 system.  In the case of DriverWorks, the DriverWorks driver is the protocol driver.  When combined with the device-specific.c4Z file it provides the custom code necessary to implement the 2-way device driver.  In the case of DriverWorks, the DriverWorks driver is the protocol driver. When combined with the device-specific.c4Z file it provides the custom code necessary to implement the 2-way device driver.
