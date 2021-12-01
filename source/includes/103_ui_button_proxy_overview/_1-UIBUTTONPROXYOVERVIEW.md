## UI BUTTON PROXY OVERVIEW

The UI Button Proxy was delivered in OS 2.9.0. The proxy supports the display of a configurable button within Navigator. The button and can be placed onto any experience menu such as Listen, Watch, Security, Comfort. Navigator menu configuration for shortcuts supported by the button is done through ComposerPro's standard room menu controls.The button's icon can also change to reflect the state of the device that the button controls.

The XML name of the proxy is "UI Button". For example:

`<proxies>`
  `<proxy proxybindingid="5001" name="UI Button">uibutton</proxy>`
`</proxies>`


To the right is an example of the connection information required to use the UI Button Proxy:

```xml
 <connections>
    <connection>
        <id>5001</id>
        <facing>6</facing>
        <connectionname>UIBUTTON</connectionname>
        <type>2</type>
        <consumer>False</consumer>
        <audiosource>False</audiosource>
        <videosource>False</videosource>
        <linelevel>False</linelevel>
        <classes>
            <class>
               <classname>UIBUTTON</classname>
         </class>
       </classes>
    </connection>
</connections>
```


Note that OS Release 2.10.0 enhanced this Proxy with the capability to allow for URL manipulation of Navigator's web module feature through the use of the HTML Web View.

### HTML WebView Overview
Adding the HTML WebView functionality to an Experience (UIbutton) driver enables the driver developer to specify a web URL that can provide an HTML interface for the end user. The web UI is launched within an embedded browser on the Control4 T3 touch screen. There is no support for WebView in the On Screen Navigator, the Flash Navigator or the mobile applications (iOS and Android).

### HTML WebView Usage Best Practice Recommendations
The Driver Developer should implement the proxy interfaces that Control4 provides as a standard part of the user 
experience to the full extent that these apply to the device. The web interface should be considered supplementary to 
the proxy interface.

The Driver Developer should keep the Web UI as simple as reasonably possible.

HTML WebView Usage Guidelines (rules):

The developer must self-certify their website on our current browsers (on the T3, T4s and Mobile devices). If they find any incompatibility between their HTML UI / website, and our embedded browser, they must code around it.

They must provide all support for their web UI.

The Experience driver can do no more than reference the external website, all log ins must occur at the web site, not within the driver.

There is no Control4 certification for an Experience driver that uses the HTML WebView capability.
 
Because these drivers are not certified, we reserve the right to post them or not to post them within the Control4 online database based on discretion.

If a call comes to our support, we MAY instruct the dealer to remove the driver, otherwise any support will be referred to the developer of the driver.


### JavaScript API

The Proxy has also been enhanced to  provide a JavaScript API that allows Driver hosted web views to send commands, subscribe to DATA\_TO\_UIs and variables using the existing mobile communication channels.

In addition to the standard UI Button Proxy functionality, the enhancement includes:

A new capability: [mobile\_webview\_enabled][1]

Three new [JavaScript APIs][2].

A sample Driver: Javascript API Demo.  To use the demo driver:

1. Download the Javascript API driver from the JS demo Driver folder from the DiverWorks Github repository and add it to your project.
2. Under the Project’s System Design, select the room where the driver was added.
3. Under the Room’s Properties select Navigator.
4. Note the that the demo driver (UI Button) is listed under the Device column in the following Experience Menus: Comfort, Listen, Security and Watch.
5.  Ensure that UI Button has a Visibility status of Visible in each of the Experience menus. The status can be changed by clicking on the Modify … button on the Properties screen.
6.  Refresh Navigators. Note that it may take up to 30 minutes for the UI Button to appear in the Experience Menus. 


**Demo Driver Usage **

The driver utilizes a lightbulb and color variables to demonstrate the use of the web\_view\_url capability and new APIs. Selecting the UI Button driver from System Design will display the Advanced properties for the driver.  The driver supports the selection of several states for the bulb.

<img src="images/103_1-01.png"/>

Select a state, Red for example, and click the set Button. Verify the color state is red on Touchscreens in the room where the UI Button resides and mobile devices running this project. The color state can also be verified by double clicking the UI Button driver from System design. 


<img src="images/103_1-02.png"/>

The driver’s Lua output will from the Red State setting is displayed to the right. 

```xml
OnPropertyChange():	States	Red
OnPropertyChange():	States
Icon changed to:	Red
Red
fireEvent():	Red
```

Next, from a mobile device, change the color of the bulb state to Blue. Verify the state change on Touchsrceens and double clicking the UI Button driver from System design.

The driver’s Lua output from changing from red State to Blue is displayed to the right. 

```xml
OnPropertyChange():	States	Red
OnPropertyChange():	States
Icon changed to:	Red
Red
fireEvent():	Red
OnPropertyChange():	States	Blue
Icon changed to:	Blue
OnPropertyChange():	States
Blue
fireEvent():	Blue
```


### WebView Mobile Usage Best Practice Recommendations

Webview Mobile App Usage Guidelines (rules):

When accessing a controller remotely through the App, a fully qualified URL should be used to ensure all UI resources will render correctly on the App. The mobile App cannot access local-style resources specified by the CSS. However, if the CSS is structured to include the fully qualified path including the controller syntax, the resource will be available both locally and remotely. 

For example, here is a path that would successfully render a background image locally: 

 `{ background-image: url(../images/wp_carbon_blue.jpg); padding: 16px; } ` 

However, this path will fail to render the  image on the mobile App. An example of a fully qualified URL to the background image would be: 

`{ background-image: url(controller://driver/JavascriptAPIDemo/contents/images/wp_carbon_blue.jpg); padding: 16px; }`


### Implementation
See the [web\_view\_url][3] capability


### Supported HTML/CSS Components

The following HTML/CSS components and versions are shipped with the T3 and T4 touchscreens:

**T3:**

- Mozilla 5.0
- Linux for Android 4.4.2 rk3188 Build KOT49H 
- AppleWebKit 537.36 
- KHTML, like Gecko Version 4.0 
- Chrome 30.0.0.0 
- Safari 537.36


**T4:**

- Mozilla 5.0
- Linux for Android 4.4.2 rk3188 Build KOT49H 
- AppleWebKit 537.36
- KHTML, like Gecko Version 4.0 
- Chrome 66.0.3359.158 
- Safari/537.36

[1]:	#mobile_web_view_enabled
[2]:	#ui-button-proxy-webview-javascript-api
[3]:	#web_view_url