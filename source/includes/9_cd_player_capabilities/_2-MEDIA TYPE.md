## media\_type

Media that the device is capable of playing. Bitmask values include:

- CD = 0X01
- Audio Files (mp3) = 0X2
- Video = 0X4
- Broadcast = 0X8


### Signature

`<media_type></media_type>`


| Parameter | Description |
| --- | --- |
| int | Number of discs. |


### Example

```xml
<capabilities>
   <media_type>0X2</media_type>
</capabilities>
```


