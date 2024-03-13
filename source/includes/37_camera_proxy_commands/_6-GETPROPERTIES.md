## GET\_PROPERTIES

Command called once by a UI entity to learn how to access a camera. It returns a block of XML reporting the properties of the camera.


### Name

`GET_PROPERTIES ()`


### Returns

```xml
 <camera_properties>
  <address >hostname or internet address</address>
  <http_port>port</http_port>
  <rtsp_port>port</rtsp_port>
  <authentication_required>true or false</authentication_required>
  <authentication_type>BASIC</authentication_type>
  <username>~username~</username>
  <password>password</password>
  <publicly_accessible>true or false</publicly_accessible>
</camera_properties>
```
