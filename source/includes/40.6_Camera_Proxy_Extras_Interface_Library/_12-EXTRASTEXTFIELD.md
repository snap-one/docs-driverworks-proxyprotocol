## ExtrasTextField

### Overview

This class represents abstraction of the Extras Text Field object. The class interface provides following cations:

- Initialization of an Extras Text Field object
- Setting Extras Text Field object parameters, text field mode and value


### TextFieldMode

##### Type

|Name|Value|
|---|---|
|TextFieldMode|"normal"\|"numeric"\|"alphanumeric"\|"password"|

### ExtrasTextField : ExtrasObject

 Class that represent extras checkbox functionality. This class is derived from ExtrasObject. Instance of the class can be created independently but will not be displayed alone, it should be added to the instance of the Extras class.rasTextField = inheritsFrom(ExtrasObject)

|Field Name|Field Type|
|---|---|
|TYPE|string|
|\_\_name|Methafield|
|mode|TextFieldMode|

### ExtrasTextField:construct

 ExtrasTextField constructor

#### Function Signature:

`ExtrasTextField:construct(objParams, value, mode)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objParams|ObjectParameters|For initialization of the base class|
|value|string|TextField value that will be displayed on the field in the CI|
|mode|TextFieldMode|Text field mode: password, numberic ...|

### ExtrasTextField:makeSetupXml

 Returns XML string that represents the button setup with all extraparameters

 Makes XML that should be integrated in the response to
 GET\_EXTRAS\_SETUP Proxy message.


#### Function Signature:

`ExtrasTextField:makeSetupXml()`


#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
