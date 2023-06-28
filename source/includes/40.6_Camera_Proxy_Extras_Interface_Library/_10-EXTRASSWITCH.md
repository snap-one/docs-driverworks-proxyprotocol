## ExtrasSwitch

### Overview

This class represents apstraction of the Extras Switch object. The class interface provides following cations:

- Initialization of an Extras Switch object
- Setting Extras Switch object parameters and value

### ExtrasSwitch : ExtrasObject

 Class that represent extras switch functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasSwitch = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|\_\_name|Methafield|

### ExtrasSwitch:construct

 ExtrasSwitch constructor

#### Function Signature:

`ExtrasSwitch:construct(objParams, value)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters|For initialization of the base class|
|value|string|Switch value (true, false) that will be displayed on the button in the CI|

### ExtrasSwitch:makeSetupXml

 Returns XML string that represents the button setup with all extraparameters

 Makes XML that should be integrated in the response to GET\_EXTRAS\_SETUP Proxy message.


#### Function Signature:

`ExtrasSwitch:makeSetupXml()`


#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
