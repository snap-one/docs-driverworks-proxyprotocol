## Extras Class

### Overview

This class provides an interface between instances of the ExtrasObjectBasedClass. This class can cover following use cases:

- Add/Remove/Change Extras Section of an Extras Object
- Add/Remove Extras Object
- Get instance of an existing Extras Object
- Make Extras State/Setup XML strings based on objects provided
- Update Extras Object state


### ObjectParameters

 Structure that contains all fields needed to initialize ExtrasObject instance

|Field Name|Field Type|
|---|---|
|id|string|
|command|string|
|label|string|
|hidden|string\_bool|
|readonly|string\_bool|
|extraparams|table\<string,string\>|

### Extras:addObjects

 Adds extras object to the container in the section named *sectionLabel*

New object will be added at the end of the section and will be displayed  as the last section element in the CI. In case of object array, Object order in the CI will be in the same order objects were sorted in the input array.

#### Function Signature:

`Extras:addObjects(objects, sectionLabel)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objects|ExtrasObjectBasedClass\|ExtrasObjectBasedClass: List or individual extras object|
|sectionLabel|string||

#### Returns:

|Name|Type|Description|
|---|---|---|
|cnt|number|Number of objects added|

### Extras:getObject

 Returns extras object with *id* no matter the section

#### Function Signature:

`Extras:getObject(id)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|id|string|ID of the extras object|

#### Returns:

|Name|Type|Description|
|---|---|---|
|object|ExtrasObjectBasedClass|nil||

### Extras:updateObject

 Updates *value* and *hide* parameter for the object with *objId* and sends notification to proxy bound to *proxyId*

 If *value* or *hide* is not provided, field value will not change. This methods updates fields and sends Proxy Notification that state has been changed.

#### Function Signature:

`Extras:updateObject(proxyId, objId, newValue, hide)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|objId|string|ID of the extras object|
|newValue|string|Value to be updated|
|hide|string\_bool|True or false string|

### Extras:removeObject

 Removes extras object with *id* no matter the section.

#### Function Signature:

`Extras:removeObject(id)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|id|string|ID of the extras object|

#### Returns:

|Name|Type|Description|
|---|---|---|
|ret|boolean|Returns true if removal was successful|

### Extras:makeSetupXml

 This method makes complete XML string to be send as response to GET\_EXTRAS\_SETUP proxy command.

#### Function Signature:

`Extras:makeSetupXml()`

#### Returns:

|Name|Type|Description|
|---|---|---|
|xml|string||
### Extras:makeStateXml

This method makes complete XML string to be send as response to GET\_EXTRAS\_STATE proxy command or to be sent after extras object update.

#### Function Signature:

`Extras:makeStateXml()`


#### Returns:

|Name|Type|
|---|---|---|
|xml|string|

### Extras:sendSetup

 Builds xml and sends proxy notification EXTRAS\_SETUP\_CHANGED

#### Function Signature:

`Extras:sendSetup(proxyId)`

### Extras:sendState

 Builds xml and sends proxy notification EXTRAS\_STATE\_CHANGED


#### Function Signature:

`Extras:sendState(proxyId)`

### Section

 Structure that represent a section. Holds section name and ExtrasObject based classes array.

|Field Name|Field Type|
|---|---|
|label|string|
|objects|ExtrasObjectBasedClass]|

### ExtrasObjectBasedClass

 This alias is for all classes that inherits the ExtrasObject class.

##### Type

|Name|Value|
|---|---|
|ExtrasObjectBasedClass|ExtrasButton, ExtrasCheckbox  |

### string\_bool

 Alias for values can be provided as hide argument

##### Type

|Name|Value|
|---|---|
|string\_bool|"true" "false"|

### Extras

 Container class for the ExtrasObject based instances (Button, Checkbox ...) This class is used to hold ExtrasObject based instances and to handle XML assembling and sending. This class handles sections as well as = inheritsFrom(nil)

|Field Name|Field Type|
|---|---|
|sections| Section |
|proxyId|number|
|has\_extras|boolean|

#### Function Parameters:

|Parameter|Type|
|---|---|---|
|proxyId|number|

### Extras:addSection

 Adds section to the instance

A *Section* table will be initialized and added in the *self.sections* field. The *object* field of the table type *Section* will bi initialized as empty table. Section order in the CI will be in the same order section were added in the container class instance.

#### Function Signature:

`Extras:addSection(label)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|label|string|Name of the section that will be displayed in the CI|

#### Returns:

|Name|Type|Description|
|---|---|---|
|ret|boolean|Returns true if insertion was successful|

### Extras:removeSection

 Removes the section with the label *sectionLabel* from the list

This method will remove the section with label *sectionLabel* and all objects in the section. Section indexes will be changed to fill
the  empty space but the order will not change.

#### Function Signature:

`Extras:removeSection(sectionLabel)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|sectionLabel|string||

#### Returns:

|Name|Type|Description|
|---|---|---|
|ret|boolean|Returns true if the operation was successful|
### Extras:getSection

 Returns section table with the label *sectionLabel*

#### Function Signature:

`Extras:getSection(sectionLabel)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|sectionLabel|string||

#### Returns:

|Name|Type|Description|
|---|---|---|
|section|Section: nil |

### Extras:changeSection

 Moves extras object with *id* in section named *newSection*

#### Function Signature:

`Extras:changeSection(id, newSection)`

#### Function Parameters:

|Parameter|Type|Description|
|---|---|---|
|id|string|ID of the extras object|
|newSection|string|Name of the new section to put the object|

### Extras:cleanCapability

This method cleans the has\_extras capability.


#### Function Signature:

`Extras:cleanCapability()`

### Extras:setCapability

This method sets the has\_extras capability.


#### Function Signature:

`Extras:setCapability()`
