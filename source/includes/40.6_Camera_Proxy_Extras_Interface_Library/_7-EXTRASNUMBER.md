## ExtrasNumber

### Overview

This class represents an abstraction of the Extras Number object. The class interface provides following cations:

- Initialization of an Extras Number object
- Setting Extras Number object parameters, number parameters

### ExtrasNumber : ExtrasObject

 Class that represent extras number functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasNumber = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|name|Methafield|
|min|number |string|
|max|number |string|
|resolution|number |string|

### ExtrasNumber:construct

 ExtrasNumber constructor

#### Function Signature:

`ExtrasNumber:construct(objParams, numberParams)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters|For initialization of the base class|
|numberParams|table\<string,number\|string\>|Table of parameters for the number functionality|

### ExtrasNumber:makeSetupXml

 Returns XML string that represents the button setup with all extra parameters

 Makes XML that should be integrated in the response to
 GET\_EXTRAS\_SETUP Proxy message.


#### Function Signature:

`ExtrasNumber:makeSetupXml()`

#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
