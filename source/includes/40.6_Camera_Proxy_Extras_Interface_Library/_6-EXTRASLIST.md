## ExtrasList

### Overview

This class represents an abstraction of the Extras List object. The class interface provides following cations:

- Initialization of an Extras List object
- Setting Extras Checkbox object parameters and list parameters
- Setting the currently selected item

### ExtrasListParameters

|Field Name|Field Type|
|---|---|
|value|string|
|maxSelections|Maximal|
|minSelections|Minimal|
|list|table\<string,string\>|

### ExtrasList : ExtrasObject

 Class that represent extras list functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasList = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|\_\_name|Methafield|
|maxSelections|number |string|
|minSelections|number |string|
|list|table \<string,string\>|

### ExtrasList:construct

 ExtrasList constructor

#### Function Signature:

`ExtrasList:construct(objParams, listParams)`

#### Function Parameters:

|Parameter|Description|
|---|---|
|objParams|ObjectParameters: For initialization of the base class|
|ExtrasListParameters|Parameters for initialization of the list|

### ExtrasList:makeListXml

 Returns the xml string needed to for response to the GET\_EXTRAS\_SETUP proxy message.

 Returns complete list tag. This tag should be a child tag of the object tag.

#### Function Signature:

`ExtrasList:makeListXml()`

#### Returns:

|Name|Type|
|---|---|---|
|mxl|string|

### ExtrasList:makeSetupXml

 Returns XML string that represents the list setup with all extra parameters

 Makes XML that should be integrated in the response to GET\_EXTRAS\_SETUP Proxy message.

#### Function Signature:

`ExtrasList:makeSetupXml()`

#### Returns:

|Name|Type|
|---|---|---|
|xml|string|
