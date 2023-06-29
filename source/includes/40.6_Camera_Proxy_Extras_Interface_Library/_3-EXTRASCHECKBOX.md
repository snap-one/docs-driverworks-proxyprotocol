## ExtrasCheckbox

### Overview

This class represents an abstraction of the Extras Checkbox object. The class interface provides following cations:

- Initialization of an Extras Checkbox object
- Setting Extras Checkbox object parameters and value


### ExtrasCheckbox : ExtrasObject

 Class that represent extras checkbox functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasCheckbox = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|name| Methafield |

### ExtrasCheckbox:construct

 ExtrasCheckbox constructor

#### Function Signature:

`ExtrasCheckbox:construct(objParams, value)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters | For initialization of the base class|
|value|string|Checkbox value (true, false) that will be displayed on the button in the CI|

### ExtrasCheckbox:makeSetupXml

 Returns XML string that represents the button setup with all extra parameters

 Makes XML that should be integrated in the response to GET\_EXTRAS\_SETUP Proxy message.

#### Function Signature:

`ExtrasCheckbox:makeSetupXml()`

#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
