## What’s New in 3.3.2

### Camera Proxy

**Support for Dynamic Camera Streams**

Camera drivers can now implement a new [dynamic streams API][1] to provide a list of streams that the Navigators can pick from. 


### Light V2 Proxy

**Capabilities that have been Added**

A new feature has been delivered in O.S. 3.3.2 which allows dealers and customers to specify how a light's brightness behaves when the light is turned on. The functionality includes:

- Preset - Light turns on to a preset level.
- Previous - Light turns on to the previous light level.
- Default On - Provided for backwards compatibility and is the same as setting Preset to On.

Driver developers must opt-in to this new feature and which parts it wants to support via the following new capabilities:

[brightness\_on\_mode\_preset][2] has been included to enable the brightness presets for "On Mode" behavior for a light.

[brightness\_on\_mode\_previous][3] has been included to enable the Previous On "On Mode" brightness  behavior for a light.

A new feature was created to allow dealers and customers to specify how a light's color behaves when a light is turned on. The functionality includes:

- Color Fade - Color behavior such as Dim to Warm
- Preset - Color changes to a preset.
- Previous - Color changes to the previous color value.
- Default On - Provided for backwards compatibility and is the same as setting Preset to On.

Driver developers must opt-in to this new feature and which parts it wants to support via the following new capabilities:

[color\_on\_mode\_fade][4] has been included to enable the Fade On "On Mode" behavior, such as Dim to Warm, for a light.

[color\_on\_mode\_preset][5] has been included to enable presets for use with "On Mode" behavior for a light.

[color\_on\_mode\_previous][6] has been included to enable the Previous On "On Mode" behavior for a light.

Additionally,  the following new capabilities have been included in 3.3.2:

A new capability: [brightness\_rate\_max][7] has been included in support of drivers without buttons. This capability allows these driver to no longer need to define click and hold maximum rates.

A new capability: [brightness\_rate\_min][8] has been included in support of drivers without buttons. This capability allows these driver to no longer need to define click and hold minimum rates.

A new capability: [supports\_brightness\_stop][9] has been included if a light brightness transition can be stopped during a ramp. 


**Capabilities that have been Deprecated**

fixed\_ramp\_rate - Use [click\_rate\_min][10] and [click\_rate\_max][11] instead.

has\_fixed\_ramp\_rate - Use [click\_rate\_min][12] and [click\_rate\_max][13] instead.

num\_buttons

ramp\_level

min\_max

on\_off

buttons\_are\_virtual


**Commands that have been Added**

Note: Enforcement of valid minimum and maximum values for many Light v2 commands are being enforced in conjunction with 3.3.2. 

A new command: [ADD\_DRIVER\_COLOR\_PRESET][14] has been included to add a new driver specific color preset.

A new command: [DELETE\_DRIVER\_COLOR\_PRESET][15] has been added to remove a driver configured color preset. 

A new command: [DYNAMIC\_OFF][16] has been added to support UIs with an off command to pair with the DYNAMIC\_ON command.

A new command: [DYNAMIC\_ON][17] has been added to allows UI's and programming to "turn on" a light involving both brightness and color in a single command

A new command [MODIFY\_DRIVER\_COLOR\_PRESET][18] has been included to change an existing driver color preset.

A new command [SET\_BRIGHTNESS\_STOP][19] has been added to stop a ramp if in progress.

A new command [SET\_COLOR\_STOP][20] has been added to stops a ramp of color if in progress.

A new command [SET\_BRIGHTNESS\_ON\_MODE][21] has been added to maintain the On preset value.

A new command [SET\_BRIGHTNESS\_RATE\_DEFAULT][22] has been added. This command is used in conjunction with generic On/Off commands to retrieve the [UPDATE\_BRIGHTNESS\_RATE\_DEFAULT][23] value.

A new command [SET\_COLOR\_ON\_MODE][24]  has beed added define color on mode.

A new command [SET\_COLOR\_RATE\_DEFAULT][25] has been added. This command is used in conjunction with generic On/Off commands to retrieve the [UPDATE\_COLOR\_RATE\_DEFAULT][26] value.

A new command [UPDATE\_BRIGHTNESS\_ON\_MODE][27] has been added to obtain how a light should turn on with regards to brightness.

A new command [UPDATE\_BRIGHTNESS\_RATE\_DEFAULT][28] has been added to provide a default value when a rate change is not provided.

A new command [UPDATE\_BRIGHTNESS\_PRESET][29] has beeb added to send a command when a press is changed.

A new command [UPDATE\_COLOR\_ON\_MODE][30] has been added to obtain how a light should turn on with regards to color.

A new command [UPDATE\_COLOR\_PRESET][31] has been added to manage On and Dim values across various brands and models of lights.

A new command [UPDATE\_COLOR\_RATE\_DEFAULT][32] has been added. This command is used in conjunction with generic On/Off commands to update the color rate default value.



**Commands that have been Modified**

The [SET\_COLOR\_TARGET][33] command has been enhanced with new parameters to support hue, saturation and presets. Additionally, this command previously included a parameter of RATE. This parameter name has changed to LIGHT\_COLOR\_TARGET\_RATE.


**Commands that have been Deprecated**

GET\_LIGHT\_LEVEL 

GET\_CONNECTED\_STATE 

GET\_PROPERTIES 


**Conditionals that have been Added**

[IS\_BRIGHTNESS][34]

[IS\_BRIGHTNESS\_TARGET][35]

[IS\_COLOR\_TARGET][36] 


**Notifications that have been Modified**

The [LIGHT\_BRIGHTNESS\_CHANGING][37] notify has been modified to include two new optional parameters: LIGHT\_BRIGHTNESS\_CURRENT\_PRESET\_ID and LIGHT\_BRIGHTNESS\_TARGET\_PRESET\_ID.

The [LIGHT\_COLOR\_CHANGING][38] notify has been modified to include parameters for Preset IDs. Additionally, this notify previously included a parameter of RATE. This parameter name has changed to LIGHT\_COLOR\_TARGET\_RATE.


The [LIGHT\_COLOR\_CHANGED][39] notify has been modified to include a parameter for a Preset ID.


**Variables that have been Added**

[Brightness Target Ramp Rate in Milliseconds][40]

[Brightness Target Rate Remaining in Milliseconds][41]


**Variables that have been Deprecated**

PRESET\_LEVEL has been deprecated as the [brightness\_on\_mode\_preset][42] capability contains this value. 

**Known Issue(s)**

_Color Lighting Control may not Work on Some Drivers_

Currently, there is a known problem with color control not working on drivers that are looking for a RATE parameter in the [SET\_COLOR\_TARGET ][43]command. The RATE parameter was not correctly implemented due to the limits of support for color rate ramping in previous versions. We are finalizing the changes to make this fully work in 3.3.2. As a result, the “RATE” parameter name has been changed to “LIGHT\_COLOR\_TARGET\_RATE”.


_Button Link Binding for Brightness Stop Functionality not Working_

A defect in 3.3.2 prevents keypad buttons bound to the Proxy’s BUTTON\_LINK binding for Brightness Stop from working. This will be resolved in 3.3.3.

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#dynamic-camera-streams
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-brightness_on-mode_preset
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-brightness_on_mode_previous
[4]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-color_on_mode_fade
[5]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-color_on_mode_preset
[6]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-color_on_mode_previous
[7]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-brightness_rate_max
[8]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-brightness_rate_min
[9]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-supports_brightness_stop
[10]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-click_rate_min
[11]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-click_rate_max
[12]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-click_rate_min
[13]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-capabilities-click_rate_max
[14]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-add_driver_color_preset
[15]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-delete_driver_-color_-preset
[16]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-dynamic_off
[17]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-dynamic_on
[18]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-modify_driver_color_preset
[19]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_brightness_stop
[20]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_color_stop
[21]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_brightness_on_mode
[22]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_brightness_rate_default
[23]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_brightness_rate_default
[24]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_color_on_mode
[25]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_color_rate_default
[26]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_color_rate_default
[27]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_brightness_on_mode
[28]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_brightness_rate_default
[29]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_brightness_preset
[30]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_color_on_mode
[31]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_color_preset
[32]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_color_rate_default
[33]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_color_target
[34]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-conditionals
[35]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-conditionals
[36]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-conditionals
[37]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-protocol-notifications-light_brightness_changing
[38]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-protocol-notifications-light_color_changing
[39]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-protocol-notifications-light_color_changed
[40]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-variables
[41]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-variables
[42]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-update_brightness_on_mode
[43]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-commands-set_color_target