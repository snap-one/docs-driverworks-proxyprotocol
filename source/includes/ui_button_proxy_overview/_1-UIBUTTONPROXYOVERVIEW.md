## UI BUTTON PROXY OVERVIEW

The UI Button Proxy was delivered in OS 2.9.0. The proxy supports the display of a configurable button within Navigator. The button and can be placed onto any experience menu such as Listen, Watch, Security, Comfort. Navigator menu configuration for shortcuts supported by the button is done through ComposerPro's standard room menu controls.The button's icon can also change to reflect the state of the device that the button controls.

The XML name of the proxy is "UI Button". For example:

`<proxies>`
  `<proxy proxybindingid="5001" name="UI Button">uibutton</proxy>`
`</proxies>`


The following is an example of the connection information required to use the UI Button Proxy:

 `<connections>
`    ` <connection>
`        `<id>5001</id>
`        `<facing>6</facing>
`        `<connectionname>UIBUTTON</connectionname>
`       ` <type>2</type>
`       ` <consumer>False</consumer>
`        `<audiosource>False</audiosource>
`       ` <videosource>False</videosource>
`        `<linelevel>False</linelevel>
`        `<classes>
`            `<class>
`                `<classname>UIBUTTON</classname>
`           ` </class>
`       ` </classes>
`    `</connection>
``</connections>
`

Note that OS Release 2.10.0 enhanced this Proxy with the capability to allow for URL manipulation of Navigator's web module feature through the use of the HTML Web View.

### HTML WebView Overview
Adding the HTML WebView functionality to an Experience (UIbutton) driver enables the driver developer to specify a web URL that can provide an HTML interface for the end user. The web UI is launched within an embedded browser on the Control4 T3 touch screen. There is no support for WebView in the On Screen Navigator, the Flash Navigator or the mobile applications (iOS and Android).

HTML WebView Usage Best Practice Recommendations
The Driver Developer should implement the proxy interfaces that Control4 provides as a standard part of the user experience to the full extent that these apply to the device. The web interface should be considered supplementary to the proxy interface.

The Driver Developer should be able to implement the driver using a URI to a hosted web UI. This web UI can be hosted on the device itself or in the cloud. The web UI should not be hosted on the Control4 controller.

The Driver Developer should keep the Web UI as simple as reasonably possible.
 
HTML WebView Usage Guidelines (rules)
- The developer must self-certify their web site on our current browser (on the T3). If they find any incompatibility between their HTML UI / website and our embedded browser, they must code around it.
- They must provide all support for their web UI.
- The Experience driver can do no more than reference the external web site, all log ins must occur at the web site, not within the driver
- There is no Control4 certification for an Experience driver that uses the HTML WebView capability.
- Because these drivers are not certified, we reserve the right to post them or not to post them within the Control4 online database based on discretion.
- If a call comes to our support, we MAY instruct the dealer to remove the driver, otherwise any support will be referred to the developer of the driver.


### Implementation
HTML WebView Overview is Implemented through the use of the `web_view_url` Capability.

`web_view_url`
Optional Capability which, when added contains the default URL that is associated with the shortcut. For example:

`<capabilities>
``<webviewurl proxybindingid="5000">http://youtube.com</webviewurl>
``</capabilities>
`
