
## What’s New in 3.4.2

### AV Proxies

The following Proxy Commands have been enhanced in this release to include a new command parameters: 

- [CONNECT\_OUTPUT][1]
- [DISCONNECT\_OUTPUT][2]
- [SET\_INPUT][3]

The new command parameters is:

- PREV\_DEV\_LIST- This parameter returns an ordered array for all devices  upstream in the AV path.



### Non-AV Proxies

**Fan Proxy**

The Fan Proxy has been enhanced in this release to include a new capability: [proxy\_fan\_speed\_connections][4]. This capability is applicable to newer fan drivers to create [BUTTON\_LINK][5] connections dynamically in association with fan speeds. 


**Keypad Proxy**

The Keypad Proxy has been enhanced in this release to include a new capability: [clear\_led\_current\_color\_support][6]. Enabling this capability allows the Keypad Proxy to clear a keypad’s button(s) color. Previously, this had to be done at the protocol level. In order to use this capability, two new Keypad Proxy commands have been delivered as well: [KEYPAD\_BUTTON\_COLOR\_CLEAR][7] & [KEYPAD\_ALL\_BUTTON\_COLOR\_CLEAR][8].


**Light V2 Proxy**

This Light V2 Proxy has been enhanced in this release with several new capabilities and a modification. These include: 

The [cold\_start][9] capability has been modified in this release to now be a [Dynamic Capability][10]. This enhancement has no impact on existing drivers currently using the cold\_start capability. Beginning with O.S release 3.4.2,  a driver can now dynamically change this capability if needed.


A new capability named [disable\_flash][11] has been included to indicates whether the driver supports Flash behavior. This capability is useful with regard to  Flash functionality being offered in the Advanced Lighting Scenes Composer Pro UI. 


A new capability named [multi\_click][12] has been included to disable multi-click events/actions for a light driver. This is useful when it is desirable to disable the ability to use press, release, single, double or triple click programming in Composer Pro.

Two new capabilities have been included to help support nesting of drivers in Composer Pro’s System Design tree. While this functionality is defined within the Light V2 Proxy, it is applicable to any Proxy and drivers that will benefit from a nested view in Composer Pro’s System Design.

The [nesting\_driver\_is\_parent][13] capability indicates whether or not a driver is dependent on other, supporting drivers. These supporting drivers will appear nested under the parent driver. This capability must be used in conjunction with the new variable:  [VAR\_C4\_NESTING\_PARENTS\_CHILD\_DEVICES][14]. This variable includes a comma delimited list of ID values for the secondary (child) drivers(s) required by the parent driver. This list represents the drivers that will be nested under the parent driver in Composer Pro.

The [nested\_driver\_is\_child][15] capability indicates whether or not this driver is a dependent driver required by primary driver for use.  When used correctly, it will setup the dependent driver(s) to be nested under the primary driver in Composer Pro. This capability must be used in conjunction with the new variable: [VAR\_C4\_NESTED\_CHILDS\_PARENT\_DEVICE][16]. 
This variable includes the ID of primary (parent) driver requiring its use. This is the associated driver with the nesting\_driver\_is\_parent capability set to true.

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#receiver-proxy-commands-connect_output
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#receiver-proxy-commands-disconnect_output
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#receiver-proxy-commands-set_input
[4]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#fan-capabilities-proxy_fan_speed_connections
[5]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#keypad-button-link-bindings-keypad-button-link-bindings
[6]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#keypad-capabilities
[7]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#keypad-proxy-commands-keypad_button_color_clear
[8]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#keypad-proxy-commands-keypad_all_button_color_clear
[9]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#light-v2-capabilities-cold_start
[10]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#camera-protocol-notifications-dynamic_capability_changed
[11]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#light-v2-capabilities-disable_flash
[12]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#light-v2-capabilities-multi_click
[13]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#light-v2-capabilities-nesting_driver_is_parent
[14]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#light-v2-variables
[15]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#light-v2-capabilities-nested_driver_is_child
[16]:	https://snap-one.github.io/docs-driverworks-proxyprotocol-342-beta/#light-v2-variables