# Light V2 Conversion Commands

This section lists the Commands used for converting to/from hue, saturation and lightness (HSV) and red, blue and green (RGB).

Control4 OS 3.3.0 and later releases include native support for Color Chromaticity and Color Correlated Temperature (CCT) functionality. Navigators, the Light V2 Proxy, and the Advanced Lighting Scene (ALS) agent use this new color architecture. This means that Drivers written against the 3.3.0 Light V2 Proxy can now implement native color support.

Color API's between the proxy, ALS agent and drivers are based on the CIE 1931 XY Chromaticity standard for visible color.

Beginning with O.S. 3.3.0, all drivers (including non-color) should implement the new Brightness Target API for communicating brightness to the Light V2 proxy.



## Understanding Chromaticity

Currently, no bulb or LED strip can produce all of the colors seen by the human eye. However, the range of colors lighting devices can produce is constantly growing. In addition to this, most lighting devices do not produce the same range of colors as other devices. In order to provide a consistent color experience in a home which could include various brands and models of bulbs or strip lighting; the Control4 color API needs to support all possible visible colors. Also, RGB and Hue/Saturation data values are not universal. The same RGB and Hue/Saturation data value across different lighting devices will often produce different actual visible colors. The use of  Chromaticity can solve these issues. 

Chromaticity allows for communicating a color using XY coordinates that is universal and can be computationally converted to various other color spaces, formats, and their respective data values. Below is a diagram showing all visible light wavelengths and their reference points according to the CIE 1931 Chromaticity standard. All visible colors can be specified by an XY coordinate.


<img src="images/64_2-01.png"/>



### The Use of Gamuts

Most light driver developers are familiar with Hue and Saturation or RGB values. Hue and Saturation are a data representation of how much of a color something is in relation to how much it can be in total. RGB is similar but also includes how much of its total brightness is used. Neither of these provide a way to verify if two different lighting devices are producing the same viewable color as seen by a home owner. 

However, if a devices’ gamut value for the RGB or Hue/Sat value is known, it is possible to compare this device with a different device’s gamut values making it possible to understand how the two device's colors relate. Below are the gamut triangles of three different LED chips, used in a lighting products.

<img src="images/64_3-02.png"/>

In the image above, you can see that Gamut B (the smaller Red triangle) can produce a far smaller range of colors than the Gamut A (Black) triangle. If we were to send the RGB data of "0,255,0" to two different devices (one device using Gamut A LED chips and another device using Gamut B LED chips) the actual visible green color light produced by both devices would be very different. 

For example, consider a home owner wants to set two different light device colors to "White" or the center of each triangle:  255,255,255 for RGB and the device gamut values are not used in their respective drivers. The resulting visual white color that the home owner would see would be very different between the two light devices. In this case, the device using Gamut B LED chips would be a much lower Color Correlated Temperature (CCT). In fact, the difference between the two devices would be over 1000. This could certainly annoy many home owners. This is why it's very useful to know the gamut of your device if it is possible to obtain it

Driver developers that know the gamut of their LED chips also know that there are standard mathematical formulas for transitioning any RGB value to/from the more universal XY Chromaticity color space.

For driver developers who do not know their LED chips gamut or aren't interested in color accuracy the provided RGB↔XY  lua conversion function can be used. Be aware that these calls map RGB and Hue/Saturation data values to the generic sRGB gamut and that the color a home owner or dealer selects on UIs may not match the color produced by the LED chips. Below is graphical representation for the sRGB gamut for reference.

<img src="images/64_2-03.png"/>



### Lack Brightness Values

Chromaticity does not include a data value for brightness. Reasons for this include:

- Many users prefer to adjust color and brightness individually, such as selecting a color then ramping brightness or picking a brightness and changing colors.

- If Color presets included brightness it would result in multiple presets of the same Red color. However, they would be at different brightness levels. This would make color preset navigation and selection for home owners cumbersome.

- Programming Event firing and Conditional checks would be very convoluted. For example, White at 50% is not be the same as White at 100%. And ultimately,  all the user wanted to check is if the color was "White".

- Similar to Programming complexity, Lighting Scene tracking would become unmanageable. Advanced Lighting Scene creation is more configurable and provides better ways for dealers to meet customers needs.



### Color Correlated Temperature (CCT)

Many colored lighting devices are designed to fulfill just the CCT implementation of color. Drivers do have the ability to specify if they support CCT, Full Color or both. Different configuration and UI features are available based on capabilities specified by the driver. Most all "full color" lights will inherently support CCT, as the image below shows. 


<img src="images/64_4-03.png"/>

Note that Control4 OS Color APIs also allow specifying if a color is CCT or "Full Color". This helps the device know if the user is trying to control the light in one mode vs another.