## ExtrasIcon

### Overview

This class represents an abstraction of the Extras Icon object. The class interface provides following cations:

- Initialization of an Extras Icon object
- Setting Extras Icon object parameters and value


### ExtrasIcon : ExtrasObject

 Class that represent extras icon functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasIcon = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|name|Methafield|

### ExtrasIcon:construct

 ExtrasIcon constructor

#### Function Signature:

`ExtrasIcon:construct(objParams, value)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters: For initialization of the base class|
|value|string|Link or path to the image that will be displayed in the CI|

### ExtrasIcon:makeSetupXml

 Returns XML string that represents the button setup with all extra parameters

 Makes XML that should be integrated in the response to
 GET\_EXTRAS\_SETUP Proxy message.

#### Function Signature:

`ExtrasIcon:makeSetupXml()`

#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
