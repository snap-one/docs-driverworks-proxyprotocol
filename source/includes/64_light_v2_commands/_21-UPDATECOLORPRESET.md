## UPDATE\_COLOR\_PRESET

Having a mandatory On color preset for all colored lights provides dealers a way of configuring various brands and models of lights in a way that a customer can have a consistent 'default on' color behavior. Without this feature, it's almost certain that different brands and models of lights would turn on to different colors or color temperatures.

In addition to the On color preset, having a mandatory Dim color preset for all colored lights provides dealers a way of configuring various brands and models of lights in a way that a customer can have a consistent 'warm dim' color behavior. 

The 'On' color preset is the color that a light should generate at its 'Default On Brightness' level.

The 'Dim' color preset is the color that a light should generate at 1% brightness. 

For example, consider a lights Default On Brightness is set to 80%. The On preset color is 4000CCT and the Dim preset color is 2000CCT. If the light was then set to a brightness level of 40%, the lights color would be 3000CCT. Also, if the lights brightness is set to 80% or higher, the color would always be 4000CCT. This formula would be used when a light is turned on (from off level) via a SET\_BRIGHTNESS\_TARGET and if no SET\_COLOR\_TARGET is additionally used. 

Any further time that SET\_BRIGHTNESS\_TARGET is used, the driver should use the formula to calculate the new color and also set that color when the brightness is changed via SET\_BRIGHTNESS\_TARGET. If a SET\_COLOR\_TARGET command is used after the light has been turned on, then the formula for warm-dim functionality should no longer occur and the color should not be auto-adjusted until the light is turned off and back on again.

When all drivers follow this formula there will be consistent On and Warm Dim lighting experiences for customers.

In 3.3.0, the LightV2 Proxy 'Dim' and 'On' color presets can be changed in Composer and Navigator. Composer currently has a checkbox to 'enable' the Dim color, although this checkbox is not an 'enable dim color' feature. It is a 'hide the dim color preset in Composer' feature. 

Upon 'disabling' the Dim color Composer is actually setting the Dim preset color to the On preset color. The LightV2 Proxy always has an On and Dim preset defined regardless of the checkbox in Composer being checked or unchecked. There isn't a 100% sure way for a driver to know if this checkbox is 'checked’.  However, a driver could consider it potentially checked if the Dim and On preset colors are not the same color.


### Signature

`UPDATE_COLOR_PRESET()`


| Parameter | Description |
| --- | --- |
|COMMAND| String - This will be one of the following strings: `"ADDED", "MODIFIED" "REMOVED"` |
|ID| Number. Preset ID |
|NAME| String. Name of the preset. |
|COLOR\_X| Double - CIE 1931 Chromaticity Color. |
|COLOR\Y| Double - CIE 1931 Chromaticity Color.  |
|COLOR\_MODE| UInt. Color Mode (0 Full Color, 1 CCT)  |



### Returns

`None`



