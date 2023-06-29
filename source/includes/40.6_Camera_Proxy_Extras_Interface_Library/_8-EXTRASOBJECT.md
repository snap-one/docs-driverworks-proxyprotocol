## ExtrasObject

### ExtrasObject

 Base class for classes that represent extras objects (button, checkbox ...) Should not create independent instance from this class This class only purpose is to be base class for extras object classesrasObject = inheritsFrom(nil)

|Field Name|Field Type|
|---|---|
|id|string|
|command|string|
|label|string|
|hidden|string\_bool|
|readonly|string\_bool|
|extraparams|table\<string,string\>|

### ExtrasObject:construct

 ExtrasObject constructor

#### Function Signature:

`ExtrasObject:construct(objParams)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters: Table of parameters needed to assemble XML|

### ExtrasObject:addExtraparam

 Adding extra parameter to the Object instance

 If extra parameter is added, tParams argument of the Proxy command will contain value of the extras object with *id*.

#### Function Signature:

`ExtrasObject:addExtraparam(id, name)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|id|string|ID of the extras object that will be connected|
|name|string|of the extras object that will be connected|

### ExtrasObject:removeExtraparam

 Removing extra parameter from the list

 This method will remove extra parameter with *id* and value of that extras object will not be received in proxy command.

#### Function Signature:

`ExtrasObject:removeExtraparam(id)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|id|string||

### ExtrasObject:getStateXml

 Returns XML string that represents extras object state

 This string should be incorporated in response to GET\_EXTRAS\_STATE command. *id* and *value* fields will be escaped and integrated in the string. The string will be return in the following command:
\``- \<object id= "\[self.id]" value="\`self.value" /\>
\`\`
#### Function Signature:

`ExtrasObject:getStateXml()`


#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||

### ExtrasObject:getExtraparamsXml

 Returns XML string that represents list of extraparameters

 This string should be incorporated in response to GET\_EXTRAS\_SETUP Key and value of the *extraparams* field will be escaped end integrated in the message.


#### Function Signature:

`ExtrasObject:getExtraparamsXml()`


#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||

### ExtrasObject:update

Update extras object individually.

This method should be called when the user wants to udate an object individually. The method from the Extras class will update all objects, this method will update just this on object. Also, this method is inherited by all ExtrasObjectBasedClass instances.

#### Function Signature:

ExtrasObject:update(value, hidden)

### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|value|string|New value for the extras object|
|hidden|string|Hide the object or not|
## ExtrasSlider : ExtrasObject

 Class that represent extras slider functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasSlider = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|\_\_name|Methafield|
|min|number\|string|
|max|number\|string|
|resolution|number\|string|

## ExtrasSlider:construct

 ExtrasSlider constructor

### Function Signature:

`ExtrasSlider:construct(objParams, sliderParams)`

### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters: For initialization of the base class|
|sliderParams|table\<string,number\|string\>|Table of parameters for the slider functionality|

## ExtrasSlider:makeSetupXml

 Returns XML string that represents the button setup with all extra parameters

 Makes XML that should be integrated in the response to
 GET\_EXTRAS\_SETUP Proxy message.


### Function Signature:

`ExtrasSlider:makeSetupXml()`


### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
## ExtrasObject

 Base class for classes that represent extras objects (button, checkbox ...) Should not create independent instance from this class This class only purpose is to be base class for extras object classesrasObject = inheritsFrom(nil)

|Field Name|Field Type|
|---|---|
|id|string|
|command|string|
|label|string|
|hidden|string\_bool|
|readonly|string\_bool|
|extraparams|table\<string,string\>|

## ExtrasObject:construct

 ExtrasObject constructor

### Function Signature:

`ExtrasObject:construct(objParams)`

### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters: Table of parameters needed to assemble XML|

## ExtrasObject:addExtraparam

 Adding extra parameter to the Object instance

 If extra parameter is added, tParams argument of the Proxy command will contain value of the extras object with *id*.

### Function Signature:

`ExtrasObject:addExtraparam(id, name)`

### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|id|string|ID of the extras object that will be connected|
|name|string|of the extras object that will be connected|

## ExtrasObject:removeExtraparam

 Removing extra parameter from the list

 This method will remove extra parameter with *id* and value of that extras object will not be received in proxy command.

### Function Signature:

`ExtrasObject:removeExtraparam(id)`

### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|id|string||

## ExtrasObject:getStateXml

 Returns XML string that represents extras object state

 This string should be incorporated in response to GET\_EXTRAS\_STATE command. *id* and *value* fields will be escaped and integrated in the string.The string will be return in the following command:
`- \<object id= "\[self.id]" value="\[self.value]" /\>`

### Function Signature:

`ExtrasObject:getStateXml()`


### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||

## ExtrasObject:getExtraparamsXml

 Returns XML string that represents list of extraparameters

This string should be incorporated in response to GET\_EXTRAS\_SETUP Key and value of the *extraparams* field will be escaped end integrated in the message.


### Function Signature:

`ExtrasObject:getExtraparamsXml()`


### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||

## ExtrasObject:update

Update extras object individually.

This method should be called when the user wants to update an object individually. The method from the Extras class will update all objects, this method will update just this on object. Also, this method is inherited by all ExtrasObjectBasedClass instances.

### Function Signature:

ExtrasObject:update(value, hidden)

## Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|value|string|New value for the extras object|
|hidden|string|Hide the object or not|
