## What’s New in 3.4.0

### Blind Proxy

A new capability has been added to the proxy called [always\_send\_level][1]. If value is true, then the SetTargetLevel commands are always sent regardless of current level values. This is useful if the blind device does not support two-way communication and is controlled outside of the Control4 operating system. 


### Camera Proxy

Beginning with O.S. 3.4.0, camera drivers have the ability to distribute audio to devices running Navigator. If a camera supports the proper [CODEC][2] and the camera microphone has been enabled in the appropriate interface a new audio button will appear at the bottom of the single-camera view. This will allow the user to hear live audio with the live video.


### Generic Media Player Proxy

A new capability has been added to the proxy called [allow\_audio\_pathing][3]. This capability is applicable in the scenario where the AV Switch proxy is included as a secondary proxy to the Generic Media Player Proxy. It is useful  when modeling streaming media devices that require minidrivers.


### Light (v2) Proxy

The following color conversion functions have been modified in 3.4.0. The gamut parameter now receives a new valid string of: "custom”. See the links below for more information.

RGB functions:
- [ColorRGBtoXY][4]
- [ColorXYtoRGB][5]

HSV functions:
- [ColorHSVtoXY][6]
- [ColorXYtoHSV][7]

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#blind-capabilities-always_send_level
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#camera-audio-distribution
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#generic-media-player-capabilities-allow_audio_pathing
[4]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-conversion-commands-colorrgbtoxy
[5]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-conversion-commands-colorxytorgb
[6]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-conversion-commands-colorhsvtoxy
[7]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#light-v2-conversion-commands-colorxytohsv