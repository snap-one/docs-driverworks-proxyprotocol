## media type

Media that the device is capable of playing. Bitmask of:

- CD = 0X01
- Audio Files (mp3) = 0X2
- Video = 0X4
- Broadcast = 0X8


### Signature

`<media_type></media_type>`


| Parameter | Description |
| --- | --- |
| int | nMediaTypeBitmask |


### Returns

`None`


### Example

```xml
<capabilities>
   <media_type>true</media_type>
</capabilities>
```
