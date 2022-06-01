
## ColorHSVtoRGB
This function converts an HSV color to the RGB color space.


_This function was released in conjunction with O.S. 3.3.0._


### Signature

`C4:ColorHSVtoRGB (h, s, v, rgbScale)` 


### Parameters

| Parameter | Description |
| --- | --- |
| num | Number representing hue component of HSV. |
| num | Number representing saturation component of HSV. |
| num | Number representing value component of HSV. |
| num | (Optional) Number representing RGB scale (1 to 255), default value 255. |


### Returns

| Parameter | Description |
| --- | --- |
| num | Number representing the red component of RGB (in given scale). |
| num | Number representing the green component of RGB (in given scale). |
| num | Number representing the blue component of RGB (in given scale). |


### Example

```lua
lua
print(C4:ColorHSVtoRGB(80, 100, 50))
```

