## What’s New in 3.3.1

**Light V2 Proxy**

The capability: [color\_trace\_tolerance][1] has been modified to accept a Delta value of \> .01. When provided, the CIELa*b* tolerance formula is used to determining if a color is the as another color in the system.

The following Conversion Commands have been enhanced to include an optional parameter: gamut. This parameter allows for the specification of a gamut type for use in the conversions.

- [ColorHSVtoXY][2]
- [ColorXYtoHSV][3]
- [ColorRGBtoXY][4]
- [ColorXYtoRGB][5]


**Camera Proxy**

The Camera Proxy documentation has been has enhanced to include new information regarding:


- [Camera Streams][6]
- [Driver Support for Multiple Streams][7]
- [Support for Caching URLS][8]
- [Support for The Extras Interface Library][9] 


A new command: [GET\_STREAM\_URLS][10] has been added. It is used to obtain URLs for a camera that does not have a constant URL like a Cloud based camera or for cameras that have a wider range of features and configurable options that can produce better customer experiences using various client

A new notification: [STREAM\_URLS\_READY][11] has been added. This notify is used as a follow up to a GET\_STREAM\_URLS Synchronous call. This Notify will let a UI know that the URL information they requested is ready. 


New capabilities added to the Camera proxy include:  

- [dynamic\_urls\_use\_type][12]
- [requires\_dynamic\_stream\_urls][13]


Dynamic Presets are now supported within the Camera Proxy.  The following preset functionality has been include: 

- Save new presets.
- Change preset name.
- Recapture/update existing preset.
- Reorder presets.
- Delete a preset.

Dynamic Presets require the following new Capability:

- [has\_dynamic\_presets][14]

Dynamic Presets require the following new Notifications:

- [DYNAMIC\_URLS\_CHANGED][15]

Dynamic Presets require the following new Commands:

- [SELECT\_PRESET][16]
- [CHANGE\_PRESET\_NAME][17]
- [MODIFY\_PRESET][18]
- [DELETE\_PRESET][19]
- [CHANGE\_PRESET\_ORDER][20]


The following existing Camera Proxy capabilities are now Dynamic Capabilities:

- [has\_pan][21]
- [has\_tilt][22]
- [has\_zoom][23]
- [has\_home][24]

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#color_trace_tolerance
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#colorhsvtoxy
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#colorxytohsv
[4]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#colorrgbtoxy
[5]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#colorxytorgb
[6]:	hhttps://snap-one.github.io/docs-driverworks-proxyprotocol/#camera-streams
[7]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#driver-support-for-multiple-streams
[8]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#support-for-caching-urls
[9]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#camera-proxy-extras-interface-library
[10]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#get-stream-urls
[11]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#stream_urls_ready
[12]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#dynamic_urls_use_type
[13]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#requires_dynamic_stream_urls
[14]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#has-dynamic-presets
[15]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#dynamic_urls_changed
[16]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#select-preset
[17]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#change-preset-name
[18]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#modify-preset
[19]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#delete-preset
[20]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#change-preset-order
[21]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#has-pan
[22]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#has-tilt
[23]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#has-zoom
[24]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#has-home