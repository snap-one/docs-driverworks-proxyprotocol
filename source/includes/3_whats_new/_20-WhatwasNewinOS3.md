
## What was New in O.S.3

### Proxies that were Modified\*\* 
**KeyPad Proxy**

New Button Linking functionality has been added to the Proxy. Button Linking supports the ability of a driver interacting with a second driver using Button State and Button LED State. 


**Light (V2) Proxy**
LightV2 Proxy has been significantly enhanced in this release. It is recommended that Light Driver writers thoroughly review the Proxy content in this release. The changes included not only impact drivers written against OS 3. Previously delivered Light Proxy elements have been modified or in some cases deprecated. 

In OS 3, the proxy has been conceptually split into two components. The first being a Wall Control/Keypad portion and the second is a redesigned Light portion.The Light portion has been developed as a Bulb Library. The ultimate goal of the Bulb Library is to support ,more versatility for drivers to interrogate, group, control and manage individual drivers and bulbs. Bulb color, target level, minimum and maximum levels, cold start timing and other features are implemented in the Bulb Library. Dynamic Capabilities have also been added to the Light Portion. Note that all changes maintain backwards compatibility for driver side interaction. However, Navigators will have functionality deprecated due to performance reasons or improved ways of communicating with the driver.


**Media Service Proxy**
Favoriting: In conjunction with the ability to "Favorite" Navigator UI screens in OS 3, drivers written using the Media Service Proxy can now provide the ability for end users to designate favorite media delivered through an Media Service Proxy driver such as Playlists, Albums, Tracks, Stations, Movies, TV Shows, etc. 

DashboardChanged Event: The DashboardChanged event now includes content on the use of custom icons and actions.

Driver Notification Context Example: New code examples on have been added to the Media Service Proxy Driver Notification Prototype section in the Appendix.


** Best Practices**
A new section called Best Practices has been added to the Proxy and Protocol Guide. This section contains information regarding the use cases that fall outside of the typical Proxy/Protocol driver implementation. This release contains Best Practice content on the following:

Using the new Proxy-less command UPDATE PROPERTY. This is a non proxy-specific function that can be called from any device to change a property of any other device.

OS 3 Navigator UI and Volume Control - Managing Volume Commands in conjunction with the use of OS 3's new volume control slider on the Control4 UI.



