## Light Proxy Registered Variables

Lights that used the new v2 Lighting Proxy have several registered variables that can be manipulated. Note that for a switch, only the Light State variable exists.

Light State (ID=1000) - Boolean indicating if the light is on/off. If you set this variable to true on a dimmer, it will go to the preset level.

Light Level (ID=1001) - Integer indicating the current level for a dimmer. The value should be between 0-100.

Click Rate Up (ID=1002) - Integer indicating the number of milliseconds for a dimmer to ramp from 0% to 100% if it is 'clicked'. It is possible for a protocol to hide this variable after using the [`hide_proxy_properties`][1]capability in the c4i/c4z file. 

Click Rate Down (ID=1003) - Integer indicating the number of milliseconds for a dimmer to ramp from 100% to 0% if it is 'clicked'. It is possible for a protocol to hide this variable after using the `hide_proxy_properties`capability in the c4i/c4z file. 

Hold Rate Up (ID=1004) - Integer indicating the number of milliseconds for a dimmer to ramp from 0% to 100% if it is 'held'. It is possible for a protocol to hide this variable after using the `hide_proxy_properties`capability in the c4i/c4z file. 

Hold Rate Down (ID=1005) - Integer indicating the number of milliseconds for a dimmer to ramp from 100% to 0% if it is 'held'. It is possible for a protocol to hide this variable after using the `hide_proxy_properties`capability in the c4i/c4z file. 

Preset Level (ID=1006) - Integer indicating what level a light should got to when it is turned on. It is possible for a protocol to hide this variable after using the `hide_proxy_properties` capability in the c4i/c4z file. 

Max on Level (ID=1007) - Integer indicating how high the light can go with a click. To go passed the max (still capped at 100%), you need to press and hold. It is possible for a protocol to hide this variable after using the `hide_proxy_properties`capability in the c4i/c4z file. 

Min on Level (ID=1008) - Integer on how low the light will go before turning completely off. It is possible for a protocol to hide this variable after using the `hide_proxy_properties`capability in the c4i/c4z file. 

Cold Start Level (ID=1009) - Integer of what level to go to when first turning on before attempting to do a ramp. It is possible for a protocol to hide this variable after using the `hide_proxy_properties`capability in the c4i/c4z file. 

Cold Start Time (ID=1010) - Integer indicating the amount of time in milliseconds to stay at the cold start level before starting a ramp. It is possible for a protocol to hide this variable after using the `hide_proxy_properties` capability in the c4i/c4z file. 

### Usage Note

If a protocol driver doesn't support a particular capability (e.g., doesn't support cold-start), the corresponding registered variables won't exist. Even if certain variables don't exist it will not affect the IDs of the remaining variables.

[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#hide-proxy-properties