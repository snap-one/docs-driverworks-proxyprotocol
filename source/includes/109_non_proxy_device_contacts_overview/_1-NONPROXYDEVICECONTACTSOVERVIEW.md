## CONTACTS OVERVIEW

This area of the Proxy and Protocol Guide contains information for a developing a Contact driver. Contacts are unique in how they are handled within Control4's architecture. Contact drivers do not rely upon a proxy as most traditional drivers do. In the most simple use case, a contact driver is added to a project to provide icons on devices running Navigator for the contacts' state (open and close) or a change to that state. An example of this type of driver can be seen in the `contactsingle_contactswitch.c4i` file. In a typical ComposerPro installation, this driver can be found in the following directory:

`C:\Program Files\Control4\Composer###\Drivers\Virtual`

Opening this driver in a text editor and reviewing several of the driver components is helpful in order to understand how a simple contact driver is used. To begin with, line 46 of this driver defines its proxy type. The value entered here is the filename of the driver without the .c4i file extension:

`<proxy>contactsingle_contactswitch_c4</proxy>`

The filename of the driver is used in the proxy tag because this driver does not reference a defined Control4 proxy. This is a required convention for all “Combo-drivers”. Populating the proxy tag in this manner is required for the driver to work.

The next section of code to review is the states section where icons are included. Beginning with line 49 we can see that this driver has two states: Open and Closed. These states are supported by icons that are loaded onto the controller upon installation of ComposerPro. The icons to the right represent the default icon for a contact switch:

```xml
<states>
   <state>
    <id>1</id>
    <small>devices_sm\contactsingle_contactswitch_open.gif</small>
    <large>devices_lg\contactsingle_contactswitch_open.gif</large>
   </state>
   <state>
     <id>2</id>
     <small>devices_sm\contactsingle_contactswitch_close.gif</small>
     <large>devices_lg\contactsingle_contactswitch_close.gif</large>
   </state>
</states>
```


Default icons vary based on the type of contact being represented by the driver. In the example to the right, if we look at the states section from the `contactsingle_gate_c4i` file (located in the same directory) we'll see different icons being used:


```xml
<states>
   <state>
    <id>1</id>
    <small>devices_sm\contactsingle_gate_open.gif</small>`
    <large>devices_lg\contactsingle_gate_open.gif</large>`
   </state>
   <state>
    <id>2</id>
    <small>devices_sm\contactsingle_gate_close.gif</small>`
    <large>devices_lg\contactsingle_gate_close.gif</large>`
   </state>
</states>
```


Next, to the right we can examine the connection section of this driver we see the following: 

```xml
<connections>
   <connection>
     <id>1</id>
     <facing>6</facing>
     <connectionname>Contact Sensor</connectionname>
     <type>1</type>
     <consumer>True</consumer>
     <audiosource>False</audiosource>
     <videosource>False</videosource>
     <linelevel>False</linelevel>
     <classes>
      <class>
       <classname>CONTACT_SENSOR</classname>
      </class>
    </classes>
   </connection>
</connections>
```

All of the stock contact drivers use a connection type of 1. This is a control connection type and a requirement for the driver.

Finally, the last piece of driver code which needs to be considered is the control tag. If we look at the control value for the contact driver we see the following:

`<control>control4_contactsingle</control>`

Populating the control tag with the `control4_contactsingle` value in this manner is required for the driver to work.

Control4 provides stock contact drivers for the following devices:

- Carbon Monoxide Detector
- Generic Contact
- Doorbell
- Door Contact Sensor
- Driveway Sensor
- Garage Door Sensor
- Gate
- Glass Break Detector
- Heat Detector
- Humidity Sensor
- IR Beam
- Motion Sensor
- Pressure Sensor
- Smoke Detector
- Water Sensor
- Window Contact Sensor

If the device that you would like to include in a ComposerPro project falls under one of the device types listed above, it can easily be supported through one of the stock contact drivers delivered through ComposerPro. This assumes, that your driver needs consist of a simple communication protocol which will reflect contact state on UI devices using stock icons. Driver needs that fall outside of the scope of this document are currently not supported through the Contact driver architecture.