# Generic Media Player and Coverart


Media cover art can be displayed on the UI in two ways. The first process involves the coverart image being sent directly to the UI using the device protocol. The image is converted to a .jpg file and stored in the following location on the device:

`/media/images/mediaplayer/<device_id>/coverart.jpg`

In the path above, \<device\_id\> is the id of the media player. See the NEW\_COVER\_ART notify below.

The second way to display cover art is to send a URL which represents the image location from the device proxy directly to the UI. See the COVERART\_PATH\_CHANGED notify below.

Also, the proxy supports receiving three cover art image formats: 

- RGB565
- RGB888
- JPEG files 

Note that these images must be BASE64 encoded before reaching the proxy. The image is received by the proxy in one of the encoded formats from the media player using the SendToProxy: (“COVERART”) notification. Image information is sent with this notification along with the encoded image, including image width, height and format.