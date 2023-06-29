## ExtrasButton

### Overview

This class represents an abstraction of the Extras Button object. The class interface provides following cations:

- Initialization of an Extras Button object
- Setting Extras Button object parameters (label, button text, etc)


### ExtrasButton : ExtrasObject

Class that represent extras button functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasButton = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|name|string|
||text|

### ExtrasButton:construct

 ExtrasButton constructor

#### Function Signature:

`ExtrasButton:construct(objParams, text)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters|For initialization of the base class|
|text|string|Button text that will be displayed on the button in the CI|

### ExtrasButton:makeSetupXml

 Returns XML string that represents the button setup with all extra parameters

 Makes XML that should be integrated in the response to
 GET\_EXTRAS\_SETUP Proxy message.

#### Function Signature:

`ExtrasButton:makeSetupXml()`


#### Returns:

|Name|Type|
|---|---|
|xml|string|

### ExtrasButton:getStateXml

 Returns XML string that represents extras object state

 This method overrides the method from the base class. This string should be incorporated in response to GET\_EXTRAS\_STATE
 command. *id* and *value* fields will be escaped and integrated in the string.
 
The string will be return in the following command:
 `- \<object id= "\[self.id]" value="\[self.value]" /\>`

#### Function Signature:

`ExtrasButton:getStateXml()`


#### Returns:

|Name|Type|
|---|---|
|xml|string|
