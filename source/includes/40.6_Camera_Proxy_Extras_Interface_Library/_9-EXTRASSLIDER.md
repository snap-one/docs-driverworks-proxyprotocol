## ExtrasSlider

### Overview

This class represents an abstraction of the Extras Slider object. The class interface provides following cations:

- Initialization of an Extras Slider object
- Setting Extras Slider object parameters and slider parameters

### ExtrasSlider : ExtrasObject

 Class that represent extras slider functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasSlider = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|name|Methafield|
|min|number|string|
|max|number|string|
|resolution|number|string|

### ExtrasSlider:construct

 ExtrasSlider constructor

#### Function Signature:

`ExtrasSlider:construct(objParams, sliderParams)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters|For initialization of the base class|
|sliderParams|table\<string,number\|string\>|Table of parameters for the slider functionality|

### ExtrasSlider:makeSetupXml

 Returns XML string that represents the button setup with all extraparameters

 Makes XML that should be integrated in the response to
 GET\_EXTRAS\_SETUP Proxy message.


#### Function Signature:

`ExtrasSlider:makeSetupXml()`


#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
