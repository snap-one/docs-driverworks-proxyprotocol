## URL\_CHANGED

Notification that supports the ability for the driver to dynamically change the web URL. This is useful in cases such as changing ports, load balancing and driver-delivered controller hosted UI content. This function is sent to the proxy when the URL changes. Note that if the parameter value is empty, then the URL is considered disabled and the web view will not be shown in navigator. Also, note, Navigator will not change the URL of an open web view.


### Signature

`URL_CHANGED` 


| Parameter | Description |
| --- | --- |
| url | str: Value of the URL |


### Returns

`None`


### DataToUI

Sends “url” DataToUI: `<url>http://google.com</url>`


### Example

`C4:SendToProxy(5001, "URL_CHANGED", {url="http://control4.com"})`


### Usage Note

See the HTML Webview Overview content for more information.