
## ColorXYtoCCT
This function converts from a CIE-1931 xy chromaticity to a CCT (color temperature in Kelvin) color.


_This function was released in conjunction with O.S. 3.3.0._


### Signature

`C4:ColorXYtoCCT (x, y)`


### Parameters

| Parameter | Description |
| --- | --- |
| num | Number representing the x component of a CIE-1931 xy chromaticity. |
| num | Number representing the y component of a CIE-1931 xy chromaticity. |


### Returns

| Parameter | Description |
| --- | --- |
| num | Number representing the CIE-1931 xy chromaticity as a Kelvin temperature. |


### Usage Note

This function will return a color temperature for any value provided. This includes color values that fall outside of the usual white/CCT colors.


