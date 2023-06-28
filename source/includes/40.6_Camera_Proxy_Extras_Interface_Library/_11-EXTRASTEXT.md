## ExtrasText

### Overview

This class represents an abstraction of the Extras Text object. The class interface provides following cations:

- Initialization of an Extras Text object
- Setting Extras Text object parameters and value

### ExtrasText : ExtrasObject

Class that represent extras text functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasText = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|name|Methafield|

### ExtrasText:construct

 ExtrasText constructor

#### Function Signature:

`ExtrasText:construct(objParams, value)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters|For initialization of the base class|
|value|string|Text value that will be displayed on the element in the CI|

### ExtrasText:makeSetupXml

 Returns XML string that represents the button setup with all extraparameters

 Makes XML that should be integrated in the response to GET\_EXTRAS\_SETUP Proxy message.


#### Function Signature:

`ExtrasText:makeSetupXml()`


#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
